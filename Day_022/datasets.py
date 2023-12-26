import requests
import pandas as pd
import csv
import json
from os import remove

url = 'https://archive.ics.uci.edu/ml/datasets.php'
df = pd.read_html(requests.get(url).content)[5]
# noinspection PyTypeChecker
df.to_csv('22_Day_Web_scraping\scrapped_data.csv', header=None)


# noinspection PyPep8Naming
def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['Name']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


csvFilePath = r'22_Day_Web_scraping\scrapped_data.csv'
jsonFilePath = r'22_Day_Web_scraping\scrapped_datasets.json'
make_json(csvFilePath, jsonFilePath)
remove(r'22_Day_Web_scraping\scrapped_data.csv')
