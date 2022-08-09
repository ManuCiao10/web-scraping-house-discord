import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from bs4 import BeautifulSoup


class Roomlala:
    def __init__(self):
        self.base_url = "https://en-ca.roomlala.com/rent/CA-Canada/quebec-city-area"
        self.params = {'nightRateMin': '10', 'nightRateMax': '500'}
        self.session = requests.Session()
        page = self.session.post(self.base_url, data=self.params)
        print(page)
        #soup = BeautifulSoup(page.content, 'lxml')


if __name__ == "__main__":
    Roomlala()

# https://discord.com/api/webhooks/1006323255063351306/Hk7YU1XxxX3GIPOMf7ii2TYYz2-FNUIhRxU785QFxQlnKZIAl-bo5o-NNTQi5N79ghxk
