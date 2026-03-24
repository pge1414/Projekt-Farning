#https://realpython.com/python-web-scraping-practical-introduction/
#https://brightdata.de/blog/web-data-de/how-to-scrape-news-articles
#https://brightdata.com/blog/how-tos/beautiful-soup-web-scraping
#https://beautiful-soup-4.readthedocs.io/en/latest/#navigating-the-tree
#https://www.geeksforgeeks.org/python/multiprocessing-python-set-1/
#notion.site
#["([['a']])"] - wie bekomme ich die unnötigen klammern weg, so dass danach nur eine liste mit einem a drin steht? - url.append(u.values()[0]) - so könnte

#Problem: links.json muss stets geleert werden, damit die neuen Links hinzugefügt werden können, da sonst die alten Links mit den neuen vermischt werden. Lösung: links.json wird mit jedem neuen Link überschrieben, damit nur die neuen Links gespeichert werden.
#str(urlf) in link.get("href", "") and 

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import certifi
import csv
import json
import tqdm
import requests
import multiprocessing

context = ssl.create_default_context(cafile=certifi.where())
url = []
wörter = []
threads = []



def scrape_link(urlf):
    links = []
    
    if requests.get(urlf).status_code == 200:
        page = urlopen(urlf, context=context)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href", "")
            if href not in url:
                if not href.endswith(".pdf") and href.startswith(urlf):
                    links.append(href)
        with open('links.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(links)

scrape_link("https://www.handelsblatt.com")

def url_aus_csv():
    with open('links.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for i in row:
                url.append(i)
    print(url)



def links_aufrufen(url):
    wörter = []

    if requests.get(url).status_code == 200:
    
        page = urlopen(url, context=context)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.get_text().split():
            if i not in wörter and len(i) > 2:

                #print("Found!" + " "  + j)
                wörter.append(i)

        with open("found_words.json", "a") as f:
            f.write(json.dumps({url: wörter}, ensure_ascii=False) + "\n")

url_aus_csv()
for element in tqdm.tqdm(url, desc="Verarbeitung läuft"):
    links_aufrufen(element)
    scrape_link(element)

url_aus_csv()