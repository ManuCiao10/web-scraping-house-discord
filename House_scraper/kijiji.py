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
        page = self.session.get(
            f"{self.base_url}/c30349001l1700124?ll=46.813082%2C-71.207460&address=Qu%C3%A9bec%2C+QC&radius=8.0&price=__520"
        )
        if not page:
            return on_message(page.status_code, self.base_url)
        self.soup = BeautifulSoup(page.content, "lxml")
        loops = self.soup.find_all("div", class_="clearfix")
        if not loops:
            print(loops.status_code)
            print(datetime.datetime.now(), "<|NO DATA FOUND|>\n")
            time.sleep(30)
            return self.payload()
        else:
            return self.scrape_data(loops)

    def scrape_data(self, loops):
        while True:
            for loop in loops:
                try:  # ADD awaiting function
                    self.pid_list.add(loop.find("a")["href"].split("/")[-1])
                    url = loop.find("a", class_="title").get("href")
                    pid = url.split("/")[-1]
                except AttributeError as err:
                    print(datetime.datetime.now(), '<|URL NOT FOUND {}|>'.format(err))
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
                        print(datetime.datetime.now(), "<|LOCAL NOT FOUND|>\n")
                        continue
                    try:
                        img = (
                            loop.find("div", class_="image").find("img").get("data-src")
                        )
                    except AttributeError:
                        continue
                    if img == None:
                        continue
                    else:
                        data = [url, address, img, price, local]

                    with open("data.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([pid, price.rstrip().lstrip(), self.time])
                        read_len_line(csvfile, self.base_url)
                        print(datetime.datetime.now(), "<|DATA WRITTEN|>\n")
                    send_webhook(data)
                else:
                    print(datetime.datetime.now(), "<|RUNNING ANOTHER REQUESTS|>\n")
                    self.payload()
        # except ValueError as err:
        #     print(err.args)
        #     print(datetime.datetime.now(), "LOOP ISSUES\n")
        #     self.payload()


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
    time.sleep(2)


if __name__ == "__main__":
    Kijiji()
