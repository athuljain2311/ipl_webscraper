import requests
import json
import csv
import os

urls = {'runs' : 'https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/alltime-toprunsscorers.js?callback=ontoprunsscorers&_=1689770092833',
        'wickets' : 'https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/alltime-mostwickets.js?callback=onmostwickets&_=1689779828766'}

for feature,url in urls.items():
    response = requests.get(url)

    response_content = response.content.decode()

    response_content = response_content.split('(')[1]
    response_content = response_content.split(')')[0]

    response_dict = json.loads(response_content)

    key = list(response_dict.keys())[0]

    players = response_dict[key]

    count = 0

    file_name = f'all_time_runs_wickets/most_{feature}.csv'

    folder_name = os.path.dirname(file_name)

    os.makedirs(folder_name,exist_ok=True)

    with open(file_name,'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        for player in players:
            if count == 0:
                csv_writer.writerow(list(player.keys()))
                count+=1
            csv_writer.writerow(list(player.values()))
