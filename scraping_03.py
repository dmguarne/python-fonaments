import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.find_all('a', title=True)

print("Llibres:\n")
for i, llibre in enumerate(elements, start=1):
    titol = llibre["title"]
    print(f"{i}. {titol}")
