from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.hepsiburada.com/ara?q=5s")

soup = BeautifulSoup(r.content,"lxml")
results = soup.find("div", attrs={"class" : "box"})

print(results.text)
