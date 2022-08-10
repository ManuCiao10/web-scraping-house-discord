import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup

class HouseScraper:
    def __init__(self):
        self.base_url = "https://www.oklouer.com"
        self.session = requests.Session()
        page = self.session.get(f"{self.base_url}/logements/studios-lofts_1-1-2_2-1-2")
        soup = BeautifulSoup(page.content, 'lxml')
        house_list = []
        address_list = []
        while True:
            for loop in soup.find_all('div', class_="unit"):
                try:
                    address = loop.find('div',class_="col-xs-12 col-sm-6 unit-infos").find('h3').text.capitalize()
                except AttributeError as ae:
                    continue
                if address not in address_list:
                    try:
                        url = loop.find('a').get('href')
                    except AttributeError as ae:
                        continue
                    try:
                        img = loop.find('img', class_="img-responsive full-width").get('src') 
                    except AttributeError as ae:
                        continue
                    try:
                        maps = loop.find('div', class_="col-xs-12 col-sm-3 hidden-xs").find('img').get('src')
                    except AttributeError as ae:
                        continue
                    source_price = self.session.get(f"{self.base_url}{url}")
                    soup_price = BeautifulSoup(source_price.content, 'lxml')
                    try:
                        price = soup_price.find('div', class_="pull-right price").find('small').text.split(" ")[1].split("/")[0]
                    except AttributeError as ae:
                        continue
                    try:
                        info = soup_price.find('div', class_="col-xs-6 col-sm-6 infos text-left").text.rstrip().lstrip()
                    except AttributeError as ae:
                        continue
                    data = [url,address,img,maps,price,info]
                    house_list.append(data)
                    address_list.append(address)
                    send_webhook(data)

def send_webhook(data):
    webhook = DiscordWebhook(
        url="YOUR WEBHOOK" 
    ) 
    embed = DiscordEmbed(title=data[1], color="127378", url=f"https://www.oklouer.com/{data[0]}")
    embed.set_thumbnail(url=f"https://www.oklouer.com/{data[2]}")         
    embed.add_embed_field(
        name="• Contact", 
        value=data[5], 
        inline=True
    )
    # embed.set_author(
    #     name="• Location"
    # )
    embed.add_embed_field(
        name="• Price/month", 
        value=data[4],
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
    HouseScraper()

"""
-Add Rooms + bed and remove maps
"""
