from typing import Any
import House_scraper
import time

session = House_scraper.LogiScraper()

def testCase(session):
    start = time.time()
    session.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8")
    session.set_noscript(Any)
    session.set_proxy("5su3v7ljqn:mjhmrl7wk2@141.11.247.82:7046")
    end = time.time()
    print("Time taken: ", end - start)

print("Testing session creation speed with requests")
testCase(session)