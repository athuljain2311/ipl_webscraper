import requests
from bs4 import BeautifulSoup

url = 'https://www.iplt20.com/auction/2023'

response = requests.get(url).text

soup = BeautifulSoup(response,'lxml')

x = soup.find_all('div',class_='ih-pcard-sec')


final_purse = []
final_purse.append([header.text for header in x[0].find_all('th')])

count = 1
each_team = []

for team in x[0].find_all('td'):
    each_team.append(team.text.strip())
    if count % 4 == 0:
        final_purse.append(each_team)
        each_team = []
    count = count + 1


players_sold = []
players_sold.append([header.text for header in x[1].find_all('th')])

for team in x[1:10]:
    each_team = []
    each_player = []
    count = 1
    for player in team.find_all('td'):
        each_player.append(player.text.strip())
        if count % 4 == 0:
            each_team.append(each_player)
            each_player = []
        count = count + 1
    players_sold.append(each_team)


players_unsold = []
players_unsold.append([header.text for header in x[12].find_all('th')])

count = 1
each_player = []

for player in x[12].find_all('td'):
    each_player.append(player.text.strip())
    if count % 4 == 0:
        players_unsold.append(each_player)
        each_player = []
    count = count + 1

print(players_unsold)