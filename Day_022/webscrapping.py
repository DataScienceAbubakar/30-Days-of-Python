import json

import requests
from bs4 import BeautifulSoup

url1 = "https://www.bu.edu/president/boston-university-facts-stats/"
response1 = requests.get(url1)
content1 = response1.content
soup1 = BeautifulSoup(content1, 'html.parser')
tables = soup1.findAll('div', {"class": "facts-wrapper"})

list_of_tables = []

for i in tables:
    keys = []
    values = []
    temp_dict = {}
    i = str(i)
    category = i[i.find('<h5>') + 4: i.find('</h5>')]
    temp_dict['Category'] = category
    all_key_start_indexes = [x+7 for x in range(len(i)) if i.startswith('"text">', x)]
    all_key_end_indexes = [x for x in range(len(i)) if i.startswith('</p>', x)]

    for l in range(len(all_key_start_indexes)):
        keys.append(i[all_key_start_indexes[l]:all_key_end_indexes[l]])

    all_values_start_indexes = []
    for v in range(len(i)):
        if i.startswith('value">', v):
            all_values_start_indexes.append(v+7)
        if i.startswith('value-text">', v):
            all_values_start_indexes.append(v+12)
    all_values_end_indexes = [x for x in range(len(i)) if i.startswith('</span>', x)]

    for m in range(len(all_values_end_indexes)):
        values.append(i[all_values_start_indexes[m]:all_values_end_indexes[m]])

    for r in range(len(keys)):
        temp_dict[keys[r]] = values[r]
    list_of_tables.append(temp_dict)
    
# pprint(list_of_tables)
with open(r"22_Day_Web_scraping\scrapped_exercise_1.json", 'w') as fp:
    json.dump(list_of_tables, fp)
