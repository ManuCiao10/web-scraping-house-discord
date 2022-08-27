from constants import *
import csv
from utils import *


# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)


class Kijiji:
    """Class for creating Kijiji Iterators"""

    def __init__(self):
        self.base_url = KIJIJI
        self.session = requests.Session()
        self.address_list = set()
        self.proxy = set()
        self.time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        Kijiji.payload(self)

    def payload(self):
        print(datetime.datetime.now().strftime("%H:%M:%S.%f"), "<|PAYLOAD|>")
        headers = {"User-Agent": set_random_user_agent(self)}
        proxies(self)
        page = self.session.get(
            f"{self.base_url}/c30349001l1700124?ll=46.813082%2C-71.207460&address=Qu%C3%A9bec%2C+QC&radius=8.0&price=__520",
            headers=headers,
        )
        if not page:
            on_message(page.status_code, self.base_url)
        self.soup = BeautifulSoup(page.content, "lxml")
        loops = self.soup.find_all("div", class_="clearfix")
        if not loops:
            Kijiji.awaiting(self)
        else:
            Kijiji.scrape_data(self, loops)

    def scrape_data(self, loops):
        while True:
            for loop in loops[1:]:
                address = (
                    loop.find("a", class_="title").text.rstrip().lstrip().capitalize()
                )
                print(datetime.datetime.now().strftime("%H:%M:%S.%f"), "<|MONITORING|>")
                if address not in self.address_list:
                    try:
                        url = loop.find("a", class_="title").get("href")
                    except AttributeError:
                        print(
                            datetime.datetime.now().strftime("%H:%M:%S.%f"),
                            "<|URL NOT FOUND|>",
                        )
                    try:
                        price = loop.find("div", class_="price").text.split(",")[0]
                    except AttributeError:
                        continue
                    try:
                        local = (
                            loop.find("div", class_="location")
                            .find("span")
                            .text.rstrip()
                            .lstrip()
                        )
                    except AttributeError:
                        continue
                    try:
                        img = (
                            loop.find("div", class_="image").find("img").get("data-src")
                        )
                    except AttributeError:
                        continue
                    if img == None:
                        img = LOGO_IMG
                    data = [url, address, img, price, local]
                    self.address_list.add(address)
                    with open("data.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(
                            [datetime.datetime.now().strftime("%H:%M:%S.%f"), address]
                        )
                        read_len_line(csvfile, self.base_url)
                        print(
                            datetime.datetime.now().strftime("%H:%M:%S.%f"),
                            "<|DATA WRITTEN|>",
                        )
                    Kijiji.send_webhook(data)
            Kijiji.another_request(self)

    def awaiting(self):
        print(datetime.datetime.now().strftime("%H:%M:%S.%f"), "<|AWAITING|>")
        time.sleep(60)
        Kijiji.payload(self)

    def another_request(self):
        print(
            datetime.datetime.now().strftime("%H:%M:%S.%f"),
            "<|RUNNING ANOTHER REQUEST|>",
        )
        Kijiji.payload(self)

    def send_webhook(data):
        webhook = DiscordWebhook(url=f"{PREFIX}{KIJIJIWEBHOOK}")
        embed = DiscordEmbed(
            title=data[1], color=COLOR_DS, url=f"https://www.kijiji.ca{data[0]}"
        )
        embed.set_thumbnail(url=data[2])
        embed.add_embed_field(name="• Area", value=data[4], inline=True)
        embed.add_embed_field(name="• Price/month", value=f"{data[3]}$", inline=True)
        embed.set_footer(text="Kijiji_Monitor", icon_url=KIJIJI_IMG)
        embed.set_timestamp()
        webhook.add_embed(embed)
        resp = webhook.execute()
        if resp.status_code == 200:
            print(datetime.datetime.now().strftime("%H:%M:%S.%f"), "<|WEBHOOK SENT|>")
        time.sleep(2)


if __name__ == "__main__":
    Kijiji()
