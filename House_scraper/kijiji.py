import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
from constants import *

class kijiji:
    def __init__(self):
        self.base_url = KIJIJI
        self.session = requests.Session()
        page = self.session.get(
            f"{self.base_url}/c30349001l1700124?ll=46.813082%2C-71.207460&address=Qu%C3%A9bec%2C+QC&radius=8.0&price=__520")
        soup = BeautifulSoup(page.content, 'lxml')
        house_list = []
        address_list = []
        for loop in soup.find_all('div', class_="clearfix"):
            try:
                address = loop.find(
                    'a', class_="title").text.rstrip().lstrip().capitalize()
            except AttributeError:
                continue
            if address not in address_list:
                try:
                    url = loop.find('a', class_="title").get('href')
                except AttributeError:
                    continue
                try:
                    price = loop.find('div', class_="price").text.split(",")[0]
                except AttributeError:
                    continue
                try:
                    local = loop.find('div', class_="location").find(
                        'span').text.rstrip().lstrip()
                except AttributeError:
                    continue
                try:
                    img = loop.find('div', class_="image").find(
                        'img').get('data-src')
                except AttributeError:
                    continue
                if(img == None):
                    continue
                else:
                    data = [url, address, img, price, local]
                house_list.append(data)
                address_list.append(address)
                send_webhook(data)


def send_webhook(data):
    webhook = DiscordWebhook(
        url=f"{PREFIX}{KIJIJIWEBHOOK}"
    )
    embed = DiscordEmbed(
        title=data[1], color=COLOR_DS, url=f"https://www.kijiji.ca{data[0]}")
    embed.set_thumbnail(url=data[2])
    embed.add_embed_field(
        name="• Area",
        value=data[4],
        inline=True
    )
    embed.add_embed_field(
        name="• Price/month",
        value=f"{data[3]}$",
        inline=True
    )
    embed.set_footer(
        text="Mitra",
        icon_url="https://i.imgur.com/8KANDeK.jpg"
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)


if __name__ == "__main__":
    kijiji()

