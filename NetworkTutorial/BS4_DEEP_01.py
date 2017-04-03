from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

print("------ find class attribute is green")
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
print("------ find Htags")
htags = bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})
for htag in htags:
    print(htag)

print("------ find class attributes are green or red")
greenRed = bsObj.findAll("span", {"class":{"red","green"}})
print(len(greenRed))

print("------ find the text is the prince")
prince = bsObj.findAll(text="the prince")
print(prince)

print("------ find and findAll")
find_one = bsObj.find(id="text")
find_all_limit_1 = bsObj.findAll(id="text")
print(find_one.get_text())
print(find_all_limit_1[0].get_text())
