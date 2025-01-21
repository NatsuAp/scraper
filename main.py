import requests
from bs4 import BeautifulSoup

def scrape(url):

    response = requests.get(url)
    response.raise_for_status()
    soup=BeautifulSoup(response.text,'html.parser')
    question_text = soup.select_one("div.content").get_text(strip=True)
    return question_text



data = scrape("https://www.crackap.com/ap/computer-science-a/question-1-answer-and-explanation.html")
print(data)



