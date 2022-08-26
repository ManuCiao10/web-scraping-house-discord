from bs4 import BeautifulSoup
from House_scraper.constants import *
import datetime
from House_scraper.utils import *
from requests_html import HTMLSession


class Awlab:
    """Class for creating Awlab Iterators"""

    default_headers = {
        "authority": "www.aw-lab.com",
        "method": "GET",
        "path": "/on/demandware.store/Sites-awlab-it-Site/it_IT/Product-GetAvailability?format=ajax&pid=AW_22121RBA_8041591",
        "scheme": "https",
        "cache-control": "no-cache",
        "cookie": "_gcl_au=1.1.874218284.1661297789; __dfduuid=f8893f07-872d-4214-9030-ac28413590fa; __cq_uuid=bdULt7ullba6lR8XnuPgv4a1PB; OptanonAlertBoxClosed=2022-08-23T23:38:50.109Z; _ga=GA1.2.1869489426.1661297930; _gid=GA1.2.436256080.1661297930; _fbp=fb.1.1661297930307.313799298; _clck=18ueoc8|1|f4a|0; dwsid=OCdkZy3w5gOjWttVFoIIgJ_6iveLiA1e8Pmib7h5HjBxLN5SNvuRGk2V9BGiRx6-2E-OekB6IVP21b6K_P_7Lw==; dwac_1475e29a8c29e08671dad6a42b=RazARnjqbPNlKOxHT0PjCOJxLtbekoeuNos%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcJANbZlIsr2Bgh2UZD0saN6Op; cquid=||; sid=RazARnjqbPNlKOxHT0PjCOJxLtbekoeuNos; dwanonymous_106322550253ae9980e0f038b6061a90=bcJANbZlIsr2Bgh2UZD0saN6Op; __cq_dnt=0; dw_dnt=0; _fphu=%7B%22value%22%3A%225.W1MbhbHTHeJDewJtG8q.1634247081%22%2C%22ts%22%3A1661302330303%7D; countryMismatch=IT; __cq_bc=%7B%22bclg-awlab-it%22%3A%5B%7B%22id%22%3A%22AW_22121RBA%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22AW_22121RBA_8041591%22%7D%2C%7B%22id%22%3A%22AW_221QGA_MNSWNIKEA%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22AW_221QGA_MNSWNIKEA_9390664%22%7D%2C%7B%22id%22%3A%22AW_221CECCEGA%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22AW_221CECCEGA_8041540%22%7D%5D%7D; __cq_seg=0~-0.38!1~-0.20!2~0.15!3~0.35!4~-0.05!5~0.18!6~0.48!7~-0.36!8~0.46!9~0.25!f0~15~9; cto_bundle=bQugkl9ydGFIak5iNDdxUFFoaDcxb0V5OXRnemJNQVVWcEdGN09vTEdwWUdjMVBqd2tQb2IzNXZtN3NMUEMxV2liNU1jcWFucW84N1E3eVUyNHkxYzJuUFBCVlZUSERUVWhISkMlMkZoV1JLWGgyMmh3M0NXY3NQWUpaUGolMkZOTkVMUUNSMzcxbnMlMkZBV3MwZmFaZXV5MWhWWDBXNjdYdzM3VWNOdVJTb0J5V3ZGSWVaVVZUR1lWJTJGS2UzaFVReWFUall0UHBlbw; cf_chl_2=1a443562743bdad; cf_chl_prog=x14; cf_clearance=rBp1IQ5AwbcWXdi3layGDTeNOXryzLDtgoQj6moa0Gk-1661307389-0-150; __cf_bm=QTLr3pfMifxs_tpqzx4oeXBVbHRaJN1xdpdgP0wSeSQ-1661307407-0-AfZXmfT5ryZhSE9HD33xKMkfMeZg0n+/oOwe2m8MKBSm80ITxjDlW6XYhzuQIjIf5zpnMxex88M7s3UrBrqVs9w=; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Aug+23+2022+22%3A21%3A10+GMT-0400+(GMT-04%3A00)&version=6.34.0&isIABGlobal=false&hosts=&consentId=4bd552a8-9da3-451d-8f9d-42562b2c9d99&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CA%3BQC&AwaitingReconsent=false; _uetsid=bd798a20233c11edb98633cf2e537579; _uetvid=1243b4b02d3611ecabd4696673e8ff48; fanplayr=%7B%22uuid%22%3A%221661297789525-e4cbe2e1d91e76553c6eecc7%22%2C%22uk%22%3A%225.W1MbhbHTHeJDewJtG8q.1634247081%22%2C%22sk%22%3A%22bc1fec19ce53501f49cde47982473767%22%2C%22se%22%3A%22e1.fanplayr.com%22%2C%22tm%22%3A1%2C%22t%22%3A1661307671719%7D; _clsk=70w5w2|1661307672137|13|1|h.clarity.ms/collect; datadome=x38wvec3AxzSebzfOGO7X.4EUQcRe_PIIT_I1mH3csHbV-WAjoyX.gCAXNwjVGXOzgM91dg-k5qcdML9qjzCM8qMtpXk8kWByW.q.lp0BuGxInQBJ8_fOlVXGoTIbJN",
        "pragma": "no-cache",
        "referer": "https://www.aw-lab.com/uomo/scarpe/nike-air-force-1-AW_22121RBA.html?dwvar_AW__22121RBA_color=8041591",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,fr;q=0.5",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }

    def __init__(self):
        self.base_url = "https://www.aw-lab.com/"
        self.session = HTMLSession()
        self.session.headers.update(self.default_headers)
        self.time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        return self.set_proxy()

    def set_proxy(self):
        print("[Setting Proxies ...]")
        self.session.proxies = {
            "http": "http://5su3v7ljqn:mjhmrl7wk2@141.11.247.82:7046",
            "https": "http://5su3v7ljqn:mjhmrl7wk2@141.11.247.82:7046",
        }
        ip = self.session.get(
            "http://lumtest.com/myip.json", headers=self.default_headers
        ).json()
        print(ip["ip"])
        return self.payload()

    def payload(self):
        print(datetime.datetime.now().strftime("%H:%M:%S.%f"), "<|PAYLOAD|>")
        page = self.session.get(f"{self.base_url}", headers=self.default_headers)
        if not page:
            return on_message(page.status_code, self.base_url)
        self.soup = BeautifulSoup(page.content, "lxml")
        print(self.soup)


if __name__ == "__main__":
    Awlab()
