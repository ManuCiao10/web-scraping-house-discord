from constants import *
from requests_html import HTMLSession
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import logging

logger = logging.getLogger(__name__)
print(logger)

class LogiScraper:
    """Class for creating LogiScraper Iterators"""

    base_url = LOGIS_QUEBEC
    default_headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        "Sec-Fetch-User": "?1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
    }

    def __init__(self, proxy=""):
        session = HTMLSession()
        session.headers.update(self.default_headers)
        self.session = session

    def set_user_agent(self):
        print("sii")
        self.session.headers["User-Agent"] = self.generate_user_agent()

    def generate_user_agent(self):
        sn = [SoftwareName.CHROME.value]
        os = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(
            SoftwareName=sn, operating_systems=os, limit=100)
        self.user_agent = user_agent_rotator.get_random_user_agent()

    

    def set_noscript(self, noscript):
        if noscript:
            self.session.cookies.set("noscript", "1")
        else:
            self.session.cookies.set("noscript", "0")

    def set_proxy(self, proxy, verify=True):
        self.requests_kwargs.update(
            {'proxies': {'http': proxy, 'https': proxy}, 'verify': verify}
        )
        ip = self.get(
            "http://lumtest.com/myip.json", headers={"Accept": "application/json"}
        ).json()
        logger.debug(f"Proxy details: {ip}")
