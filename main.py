import requests
from bs4 import BeautifulSoup

target_url = ""
news_data = []


def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawl(url):
    html_response = make_request(url)
    for span in html_response.findAll('span', attrs={'class': 'titleline'}):
        found_first_link = span.find('a').get('href')
        if found_first_link:
            if not found_first_link.startswith("https://"):
                found_first_link = url + found_first_link
            news_data.append({"title": span.text, "link": found_first_link})


crawl(target_url)
for data in news_data:
    print(data)
