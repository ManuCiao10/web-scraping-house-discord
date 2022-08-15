from constants import *
from requests_html import HTMLSession
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import logging

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
        print("[Setting user_agent ...]")
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

