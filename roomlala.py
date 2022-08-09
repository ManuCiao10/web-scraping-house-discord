import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup


class Roomlala:
    def __init__(self):
        self.base_url = "https://en-ca.roomlala.com/rent/CA-Canada/quebec-city-area"
        self.params = {'monthRateMin': '100', 'monthRateMax': '600', 'mapRectangle' : '46.895353_-71.448909_46.697923_-71.160518'}
        self.session = requests.Session()
        page = self.session.get(self.base_url, data=self.params)
        soup = BeautifulSoup(page.content, 'lxml')
        house_list = []
        address_list = []
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
                    bedrooms = loop.find('div', class_="rooms").text.split()[3]
                except AttributeError:
                    continue
                try:
                    people = loop.find('div', class_="rooms").text.split()[0]
                except AttributeError:
                    continue
                try:
                    img = loop.find('img').get('data-src')
                except AttributeError:
                    continue
                try:
                    price = loop.find('span', class_="color-primary bold").text.split()[1]
                except AttributeError:
                    continue
                data = [url,address,img,bedrooms,price,people]
                house_list.append(data)
                address_list.append(address)
                send_webhook(data)

def send_webhook(data):
    webhook = DiscordWebhook(
        url="https://discord.com/api/webhooks/1005139827462787123/jK4Nym_Y7NyOZ2S4WRwHsJ-AJVC-C7f4mohsXMhnwAWQ3_lafNR_r2IE8n7POE5a6Pns" 
    ) 
    embed = DiscordEmbed(title=data[1], color="127378", url=f"https://en-ca.roomlala.com{data[0]}")
    embed.set_thumbnail(url=data[2])         
    embed.add_embed_field(
        name="• Price/month", 
        value=f"{data[4]}$",
        inline=True
    )
    embed.add_embed_field(
        name="• Info", 
        value=f"{data[3]} Bedrooms / {data[5]} People",
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
    Roomlala()

#https://discord.com/api/webhooks/1006626270676795413/Q1rEwEeCNW57PXvAb9oeobsX8QxzMT8tMmPk9k3JR0FUxyWffeuW2lQNRei7ibI0FLiV
