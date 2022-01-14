import requests
from requests.api import head
import csv
from secrets import API_SECRET_KEY

url = f"https://newsapi.org/v2/everything?q=covid&apiKey={API_SECRET_KEY}"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request('GET', url, headers=headers, data=[])
myjson = response.json()
ourdata = []
csvheader = ['TITLE','AUTHOR', 'DESCRIPTION', 'IMAGE_URL']

for x in myjson['articles']:
    listing = [x['title'], x['author'], x['description'], x['urlToImage']]
    ourdata.append(listing)

with open('data2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print(myjson)