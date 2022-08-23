from typing import Any
import House_scraper
import time


# logisquebec_runner = House_scraper.LogiScraper()
kijiji_runner = House_scraper.Kijiji()

# def testCase_1(logisquebec):
#     start = time.time()
#     logisquebec.set_user_agent(
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8")
#     logisquebec.set_noscript(Any)
#     logisquebec.set_proxy("5su3v7ljqn:mjhmrl7wk2@141.11.247.82:7046")
#     logisquebec.createPayload()
#     logisquebec.scrape_data()
#     end = time.time()
#     print("Time taken: ", end - start)

def testCase_2(provaaa):
    start = time.time()
    provaaa.payload()
    provaaa.scrape_data()
    provaaa.on_message()
    end = time.time()
    print("Time taken: ", end - start)

print("=======HOUSE_SCRAPER=======")
#testCase_1(logisquebec_runner)
testCase_2(kijiji_runner)



