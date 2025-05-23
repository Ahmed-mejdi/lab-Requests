import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract information from the page
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print(title)
print(content)
print(links)