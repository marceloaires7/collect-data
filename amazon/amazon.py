from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.amazon.com.br/s?k=Tablets&i=computers&rh=n%3A16364762011%2Cp_123%3A110955%7C338933%7C391242%7C46655'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

print(getdata(url))
