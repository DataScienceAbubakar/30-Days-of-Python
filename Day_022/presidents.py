import requests
import pandas as pd
import csv
import json
from os import remove

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
df = pd.read_html(requests.get(url).content)
df = df[1]
df = df.iloc[:-1]
nan_value = float("NaN")
df.replace("", nan_value, inplace=True)
df.dropna(how='all', axis=1, inplace=True)
df.to_csv('22_Day_Web_scraping\presidents.csv')


# noinspection PyPep8Naming
def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))


csvFilePath = r'22_Day_Web_scraping\presidents.csv'
jsonFilePath = r'22_Day_Web_scraping\presidents.json'
make_json(csvFilePath, jsonFilePath)
remove(r'22_Day_Web_scraping\presidents.csv')
