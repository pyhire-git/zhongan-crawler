import requests
from bs4 import BeautifulSoup

url = "https://www.zhongan.com/channel/public/publicInfo_cpjbxx2018.html"


def crawler():
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "lxml")

    pdf_li = soup.find("div", id="za-new-list")
    print(type(pdf_li))
    a = pdf_li.find_all("a")
    for link in a:
        print(link['href'])


if __name__ == "__main__":
    crawler()
