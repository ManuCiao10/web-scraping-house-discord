from .logisquebec import LogiScraper
from .oklouerQuebec import Oklouer
from .kijiji import Kijiji
# _scraper = LogiScraper()
_scraper = Kijiji()

def session():
    _scraper.payload()

def scrape_data():
    _scraper.scrape_data()

# def set_user_agent(user_agent):
#     _scraper.set_user_agent(user_agent)

# def set_noscript(noscript):
#     _scraper.set_noscript(noscript)

# def set_proxy(proxy):
#     _scraper.set_proxy(proxy)

