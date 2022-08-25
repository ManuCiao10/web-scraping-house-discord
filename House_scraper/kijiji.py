from operator import delitem
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
from constants import *
import datetime
import csv
import logging
from utils import *

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)


class Kijiji:
    def __init__(self):
        self.base_url = KIJIJI
        self.session = requests.Session()
        self.pid_list = set()
        self.time = datetime.datetime.now()
        return self.payload()

    def payload(self):
        print(datetime.datetime.now(), "<|PAYLOAD|>\n")
        page = self.session.get(
            f"{self.base_url}/c30349001l1700124?ll=46.813082%2C-71.207460&address=Qu%C3%A9bec%2C+QC&radius=8.0&price=__520"
        )
        if not page:
            return on_message(page.status_code, self.base_url)
        self.soup = BeautifulSoup(page.content, "lxml")
        loops = self.soup.find_all("div", class_="clearfix")
        if not loops:
            print(datetime.datetime.now(), "<|NO DATA FOUND|>\n")
            time.sleep(15)
            return Kijiji.payload(self)
        else:
            return Kijiji.scrape_data(self, loops)

    def scrape_data(self, loops):
        while True:
            for loop in loops:
                try:  # ADD awaiting function
                    url = loop.find("a", class_="title").get("href")
                    pid = url.split("/")[-1]
                except AttributeError as err:
                    # print(err)
                    print(datetime.datetime.now(), "<|URL NOT FOUND|>\n")
                    continue
                if pid not in self.pid_list:
                    try:

                        address = (
                            loop.find("a", class_="title")
                            .text.rstrip()
                            .lstrip()
                            .capitalize()
                        )
                    except AttributeError:
                        print(datetime.datetime.now(), "ADDRESS NOT FOUND\n")
                        continue
                    try:
                        price = loop.find("div", class_="price").text.split(",")[0]
                    except AttributeError:
                        print(datetime.datetime.now(), "PRICE NOT FOUND\n")
                        continue
                    try:
                        local = (
                            loop.find("div", class_="location")
                            .find("span")
                            .text.rstrip()
                            .lstrip()
                        )
                    except AttributeError:
                        print(datetime.datetime.now(), "LOCAL NOT FOUND\n")
                        continue
                    try:
                        img = (
                            loop.find("div", class_="image").find("img").get("data-src")
                        )
                    except AttributeError:
                        continue
                    if img == None:
                        img = "https://logos-download.com/wp-content/uploads/2020/06/Kijiji_Logo-700x382.png"
                    data = [url, address, img, price, local]
                    self.pid_list.add(pid)
                    with open("data.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([pid, price.rstrip().lstrip(), self.time])
                        read_len_line(csvfile, self.base_url)
                        print(datetime.datetime.now(), "<|DATA WRITTEN|>\n")
                    Kijiji.send_webhook(data)
                else:
                    print(datetime.datetime.now(), "<|PID ALREADY EXISTS|>\n")
                    Kijiji.payload(self)

    def send_webhook(data):
        webhook = DiscordWebhook(url=f"{PREFIX}{KIJIJIWEBHOOK}")
        embed = DiscordEmbed(
            title=data[1], color=COLOR_DS, url=f"https://www.kijiji.ca{data[0]}"
        )
        embed.set_thumbnail(url=data[2])
        embed.add_embed_field(name="• Area", value=data[4], inline=True)
        embed.add_embed_field(name="• Price/month", value=f"{data[3]}$", inline=True)
        embed.set_footer(text="Kijiji_Monitor", icon_url=KIJIJI_IMG)
        embed.set_timestamp()
        webhook.add_embed(embed)
        resp = webhook.execute()
        if resp.status_code == 200:
            print(datetime.datetime.now(), "<|WEBHOOK SENT|>\n")
        time.sleep(2)
        return resp


if __name__ == "__main__":
    Kijiji()
