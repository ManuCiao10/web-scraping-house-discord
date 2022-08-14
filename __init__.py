from logisquebec import LogiScraper

_scraper = LogiScraper()


def set_proxy(proxy, verify=True):
    _scraper.set_proxy(proxy, verify)


def generate_user_agent(self):
    _scraper.generate_user_agent(self)


def set_user_agent(user_agent):
    _scraper.set_user_agent(user_agent)


def set_noscript(noscript):
    _scraper.set_noscript(noscript)
