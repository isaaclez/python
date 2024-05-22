
import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    titulo = soup.find_all("h1")
    for titulo in titulo:
        print(titulo.text.strip())
    
web_scraper("https://cs50.harvard.edu/python/2022/weeks/2/")
    