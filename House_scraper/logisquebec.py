from .constants import *
from requests_html import HTMLSession
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import logging
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

"""
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.debug(f"Proxy details: {ip['ip']}\n")
"""

class LogiScraper:
    """Class for creating LogiScraper Iterators"""

    base_url = LOGIS_QUEBEC
    default_headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        "Sec-Fetch-User": "?1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
    }

    def __init__(self, session=None):
        session = HTMLSession()
        session.headers.update(self.default_headers)

        self.session = session
        self.request_count = 0

    def set_user_agent(self, user_agent):
        print("[Setting user_agent ...]", user_agent)
        self.session.headers["User-Agent"] = user_agent

    def set_noscript(self, noscript):
        print("[Setting Script ...]")
        if noscript:
            self.session.cookies.set("noscript", "1")
        else:
            self.session.cookies.set("noscript", "0")

    def set_proxy(self, proxy: str):
        print("[Setting Proxies ...]")
        self.session.proxies = {"http": "http://{}".format(proxy),
                                "https": "http://{}".format(proxy),
                                }
        ip = self.session.get(
            "http://lumtest.com/myip.json", headers={"Accept": "application/json"}
        ).json()
        print(ip['ip'])

    def createPayload(self):
        response = self.session.get(self.base_url)
        self.soup = BeautifulSoup(response.content, 'lxml')
        self.contents = self.soup.find_all('li')
        self.address_list = []
        #self.house_list = []

    def scrape_data(self):
        for content in self.contents:
            try:
                address = content.find('h2').text.capitalize()
            except AttributeError:
                continue
            if address not in self.address_list:
                try:
                    price = content.find(class_="prix-valeur").text
                except AttributeError:
                    continue
                try:
                    area = content.find(class_="adresse-ville").text
                except AttributeError:
                    continue
                try:
                    info = content.find(class_="box-result-unit-12A").text
                except AttributeError:
                    continue
                try:
                    img = content.find('img').get('src')
                except AttributeError:
                    continue
                try:
                    url = content.find('a').get('href')
                except AttributeError:
                    continue
                data = [url, address, img, price, area, info]
                # self.house_list.append(data)
                self.address_list.append(address)
                send_webhook(data)

def send_webhook(data):
    webhook = DiscordWebhook(
        url=f"{PREFIX}{LOGISWEBHOOK}"
    )
    embed = DiscordEmbed(
        title=data[1], color=COLOR_DS, url=f"https://www.logisquebec.com{data[0]}")
    embed.set_thumbnail(url=data[2])
    embed.add_embed_field(
        name="• Area",
        value=data[4],
        inline=True
    )
    embed.add_embed_field(
        name="• Price/month",
        value=f"{data[3]}",
        inline=True
    )
    embed.add_embed_field(
        name="• Info",
        value=f"{data[5]}",
        inline=False
    )
    embed.set_footer(
        text="LogisQuebec",
        icon_url=LOGIS_IMG
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)

