from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

for i in soup.find_all("button"):
    text = i.text.replace(u'\xa0', ' ')
    copy = i['onclick'][6:-2]
    if not text == copy:
        print(text, copy)
