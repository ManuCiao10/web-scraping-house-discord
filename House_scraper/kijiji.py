from audioop import add
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
from .constants import *
import datetime
import csv

class Kijiji:
    def __init__(self):
        self.base_url = KIJIJI
        self.session = requests.Session()
        self.pid_list = set()
        self.time = datetime.date.today()

    def payload(self):
        page = self.session.get(
            f"{self.base_url}/c30349001l1700124?ll=46.813082%2C-71.207460&address=Qu%C3%A9bec%2C+QC&radius=8.0&price=__520"
        )
        self.soup = BeautifulSoup(page.content, "lxml")

    def scrape_data(self):
        while True:
            for loop in self.soup.find_all("div", class_="clearfix"):
                try:
                    url = loop.find("a", class_="title").get("href")
                    pid = url.split("/")[-1]
                except AttributeError:
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
                        continue
                    try:
                        price = loop.find("div", class_="price").text.split(",")[0]
                    except AttributeError:
                        continue
                    try:
                        local = (
                            loop.find("div", class_="location")
                            .find("span")
                            .text.rstrip()
                            .lstrip()
                        )
                    except AttributeError:
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
                        writer.writerow([pid])
                    self.pid_list.add(pid)
                    send_webhook(data)
                else:
                    self.payload()


def send_webhook(data):
    webhook = DiscordWebhook(url=f"{PREFIX}{KIJIJIWEBHOOK}")
    embed = DiscordEmbed(
        title=data[1], color=COLOR_DS, url=f"https://www.kijiji.ca{data[0]}"
    )
    embed.set_thumbnail(url=data[2])
    embed.add_embed_field(name="• Area", value=data[4], inline=True)
    embed.add_embed_field(name="• Price/month", value=f"{data[3]}$", inline=True)
    embed.set_footer(text="Kijiji", icon_url=KIJIJI_IMG)
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)
