from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.espncricinfo.com/records/trophy/batting-most-runs-career/indian-premier-league-117').text
soup = BeautifulSoup(source,'lxml')

table = soup.find('div',class_='ds-overflow-x-auto ds-scrollbar-hide').table

table_header = table.thead
table_body = table.tbody

headers = []
for header in table_header.find_all('td'):
    headers.append(header.text)

with open('most_runs.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)

    table_rows = table_body.find_all('tr')
    for table_row in table_rows:
        arr = []
        columns = table_row.find_all('td')
        for column in columns:
            arr.append(column.text)
        csv_writer.writerow(arr)

