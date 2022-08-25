# Web-Scraping-House-Discord

## Synopsis

A simple python script to scrape House datas using the Python package `requests`
to retrieve the content and `Beautifulsoup4` to parse the retrieved
content.

## Installing Scraping-House-Discord

If you want to use latest version, install from source. To install twitter-scraper from source, follow these steps:

Linux and macOS:

```bash
git clone https://github.com/ManuCiao10/web-scraping-house-discord.git
cd House_scraper
sudo python3 setup.py install
```

Also, you can install with PyPI.

```bash
pip3 install ScaperMonitor
```

## Features

The script makes it easy for customers to find a cheap and fast home. Getting a message every time a house is posted.
Actually the script support only Discord. Will be implementate very soon a version even for Whatsapp.

#### Per House it scrapes the following information:

- Location
- url
- text
- image
- n.bedroom
- n.people
- price

#### Supported Websites:

- Roomlala
- Kijiji
- Oklouer
- Logisquebec

## Discord

`Oklouer`

<img width="440" alt="Screenshot 2022-08-09 at 15 58 38" src="https://user-images.githubusercontent.com/89024276/183749691-f8f5b713-6cf8-4f03-bc7d-52753149fec8.png">

## ADD

Improvement:

1. Try to add AWAITING FUNCTION in url to avoid the infinite loop due python can do max 999 recall function
2. add proxies or change user agent if is not loops in KIJIJI
3. Check to sned a message when the program stop to run
4. add each function for each data [img, price ecc ] ONLY WHEN THE FUNCTION IS MORE COMPLEX WITH MORE CLASS AVAILABLE in the html
5. Put each module singular and run them in a server
6. Add SQL database
7. Add color for Error output
8. Django
9. Add random User Agent
10. add payment check discord
11. Implemantation with Fast API
12. add User Interface users when he can type the price and the city

## LINK UTILS

1. https://github.com/CRutkowski/Kijiji-Scraper/tree/master/kijiji_scraper
2. https://github.com/niewiemczego/nike-stock-monitor/blob/main/nike_stock.py
3. https://github.com/yasserqureshi1/Sneaker-Monitors

## Deployment

If you would like to run this 24/7 off your personal machine I would reccomend using the free credit given with google cloud, and create a server. You can make sure it runs all the time with a npm package named PM2 which will restart if errors or crashes happen.
    
## Contributing

To contribute follow these steps:

1. Fork this repository.
2. Create a branch with clear name: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
