import requests
import json
import csv
import os

with open('url_jsons/runs_wickets_per_season.json','r') as url_file:
    urls = json.loads(url_file.read())

for year in urls:
    for role in urls[year]:
        url = urls[year][role]

        response = requests.get(url)

        response_content = response.content.decode()
        response_content = response_content.split('(')[1]
        response_content = response_content.split(')')[0]

        response_dict = json.loads(response_content)

        key = list(response_dict.keys())[0]

        file_name = f'runs_wickets_per_season/{year}_{role}.csv'

        folder_name = os.path.dirname(file_name)

        os.makedirs(folder_name,exist_ok=True)

        with open(file_name,'w') as csv_file:
            csv_writer = csv.writer(csv_file)

            batters = response_dict[key]

            column_headers = list(batters[0].keys())

            csv_writer.writerow(column_headers)

            for batter in batters:
                row = list(batter.values())

                csv_writer.writerow(row)
        