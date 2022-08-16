import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
from constants import *

class Roomlala:
    def __init__(self):
        self.base_url = ROOMLALA
        self.params = {'monthRateMin': '100', 'monthRateMax': '600',
                       'mapRectangle': '46.895353_-71.448909_46.697923_-71.160518'}
        self.session = requests.Session()
        page = self.session.get(self.base_url, data=self.params)
        soup = BeautifulSoup(page.content, 'lxml')
        house_list = []
        address_list = []
        while(True):
            for loop in soup.find('div', id="ad-list-container"):
                try:
                    address = loop.find('a').get('title')
                except AttributeError:
                    continue
                if address not in address_list:
                    try:
                        url = loop.find('a').get('href')
                    except AttributeError:
                        continue
                    try:
                        bedrooms = loop.find(
                            'div', class_="rooms").text.split()[3]
                    except AttributeError:
                        continue
                    try:
                        people = loop.find(
                            'div', class_="rooms").text.split()[0]
                    except AttributeError:
                        continue
                    try:
                        img = loop.find('img').get('data-src')
                    except AttributeError:
                        continue
                    try:
                        price = loop.find(
                            'span', class_="color-primary bold").text.split()[1]
                    except AttributeError:
                        continue
                    data = [url, address, img, bedrooms, price, people]
                    house_list.append(data)
                    address_list.append(address)
                    send_webhook(data)

def send_webhook(data):
    webhook = DiscordWebhook(
        url=f"{PREFIX}{ROOMLALAWEBHOOK}"
    )
    embed = DiscordEmbed(
        title=data[1], color=COLOR_DS, url=f"https://en-ca.roomlala.com{data[0]}")
    embed.set_thumbnail(url=data[2])
    embed.add_embed_field(
        name="• Price/month",
        value=f"{data[4]}$",
        inline=True
    )
    embed.add_embed_field(
        name="• Info",
        value=f"{data[3]} Bedrooms | {data[5]} People",
        inline=True
    )
    embed.set_footer(
        text="Roomlala",
        icon_url=ROOMLALA_IMG
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)


if __name__ == "__main__":
    Roomlala()

