from http import cookies
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup
import random

class Logis:
    def __init__(self):
        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.85'
        ]
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent, "Accept-Language": "en-US,en;q=0.5",
                   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
        self.base_url = "https://www.facebook.com/marketplace/quebec/propertyrentals?minPrice=200&maxPrice=600&exact=false&latitude=46.8005&longitude=-71.2196&radius=6"
        self.session = requests.Session()
        proxy = {"http": "http://5su3v7ljqn:mjhmrl7wk2@141.11.247.180:6690"}
        page = self.session.get(self.base_url, proxies=proxy, headers=headers)
        print(page)
        # ip = page.json()['origin']
        # print("Ip:", ip)
        soup = BeautifulSoup(page.content, 'lxml')
        print(soup.prettify())


if __name__ == "__main__":
    Logis()
