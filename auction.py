import requests
from bs4 import BeautifulSoup

url = 'https://www.iplt20.com/auction'
response = requests.get(url).text
soup = BeautifulSoup(response,'lxml')
x = soup.find_all('div',class_='ih-pcard-sec')
print(x[1].prettify())