# Made by Michael Love III
# Attempting to practice Python coding by building a functional webscraper, that saves links of page input by user.

import requests
import csv
from bs4 import BeautifulSoup
import os

os.system('cls')

page_url = input('Input URL: ')
response = requests.get(page_url)
content = response.content
headers = response.headers

soup = BeautifulSoup(content, 'html.parser')
links = []
for link in soup.find_all('a'):
    url = link.get('href')
    text = link.get_text()
    
    links.append({'URL':url, 'Description':text})

fileName = input('Save Filename: ')
with open(fileName+'.csv', 'w', encoding='utf-8', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(['URL', 'Description'])
    for row in links:
        csv_writer.writerow([str(row['URL']), str(row['Description']) ])


