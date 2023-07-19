import requests
import json
import csv
import os

with open('jsons/PointsTable_urls.json') as url_file:
    urls = json.loads(url_file.read())

for year,url in urls.items():
    response = requests.get(url)

    response_content = response.content.decode()

    response_content = response_content.split('(')[1]
    response_content = response_content.split(')')[0]

    response_dict = json.loads(response_content)

    key = list(response_dict.keys())[1]

    file_name = f'PointsTable/{year}_PointsTable.csv'

    folder_name = os.path.dirname(file_name)

    os.makedirs(folder_name,exist_ok=True)

    with open(file_name,'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        headers = list(response_dict[key][0].keys())

        csv_writer.writerow(headers)

        for team in response_dict[key]:
            csv_writer.writerow(list(team.values()))