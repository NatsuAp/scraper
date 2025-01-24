import requests
from bs4 import BeautifulSoup
import ast

tags = [
    "<p>",
    "</p>",
    "</div>",
    "<strong>",
    "</strong>",
    "<div class=\"mcontent\">",
    "<b>",
    "<ul>",
    "</b>",
    "<ul class=\"qlist\">",
    "<li>",
    "</li>",
    "</ul>",
    "<code>",
    "</code>"
    
]

def scrape():
    with open("data.txt", "w") as file:
        for i in range(1, 335):
            url = "https://www.crackap.com/ap/computer-science-a/question-"+ str(i) + "-answer-and-explanation.html"
            response = requests.get(url)
            response.raise_for_status()
            soup=BeautifulSoup(response.text,'html.parser')
            content = soup.find("div", class_="mcontent")
            contentList = list(content.children)
            content = "{}".format(content)
            for i in tags:
                content = content.replace(i, " ")
            content = "{}".format(content)
            print(content)
            file.write(content)
            file.write("\n#########################################################")
            break


scrape()



