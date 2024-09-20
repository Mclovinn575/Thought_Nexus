# Made by Michael Love III
# Attempting to practice Python coding by building a functional webscraper, that saves links of page input by user.

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os, sys
import subprocess

os.system('cls')
pathname = os.path.dirname(sys.argv[0])
current_folder = os.path.abspath(pathname)

# URL of the website you want to scrape
url = input('Input URL: ')

# Send a GET request to fetch the content
try:
    print("Attempting to contact website...")
    response = requests.get(url)
except Exception as e:
    print(f'CONNECTION ERROR: {e}')
    input()

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'lxml')
    print("Website Reached!")
    print("Collecting Data...")

    # =============================================================================
    
    "Extract the webpage Title, Links, and Paragraphs"

    # Example: Extract the title of the page
    raw_title = soup.title.string
    title = re.sub(r'[<>:"/\\|?*]', '_', raw_title)

    # Example: Extract all paragraph texts
    paragraphs_list = []
    paragraphs = soup.find_all('p')
    for idx, paragraph in enumerate(paragraphs):
        paragraphs_list.append(paragraph)

    # Example: Extract links
    links_list = []
    links = soup.find_all('a', href=True)
    for link in links:
        links_list.append(link)

    # =============================================================================

    "Save extracted data to local directory folders"

    # Extract all links from the page and save to a CSV file
    try:
        link_file = f'{title}_links.csv'
        with open(f'site_links/{link_file}', 'w', encoding='utf-8', newline='') as link_writer:
            csv_writer = csv.writer(link_writer)
            csv_writer.writerow(['Datatype','Link','Description'])
            for row in links_list:
                csv_writer.writerow(['LINK', row['href'], row.text ])
            links_path = f'site_links/{link_file}'
    except Exception as e:
        print(f'Unable to parse page Links...\n\nERROR: {e}')
        input()

    # =============================================================================

    # Extract all paragraphs from the page and save it to a CSV file
    try:
        paragraph_file = f'{title}.csv'
        with open(f'site_text/{paragraph_file}', 'w', encoding='utf-8', newline='') as p_writer:
            csv_writer = csv.writer(p_writer)
            csv_writer.writerow(['Data Type','Content'])
            num=0
            for row in paragraphs_list:
                csv_writer.writerow([f'PARAGRAPH {num}',row.text])
                num+=1
            csv_path = f'site_text/{paragraph_file}'
    except Exception as e:
        print(f"Unable to parse page text...\n\nERROR: {e}")
        input()

    # =============================================================================

    # Read Paragraph CSV to generate a mass text file
    try:
        data_file = 'AI_Data.txt'
        with open(f'AI_Data/{data_file}','w', encoding='utf-8', newline='') as ai_writer:
            for row in paragraphs_list:
                ai_writer.writelines(row.text)
            data_path = f'AI_Data/{data_file}'

        content = pd.read_csv(csv_path)
        summary_range = content.iloc[0:3]['Content']
        summary_range_list = []
        for i in summary_range:
            summary_range_list.append(i)
        summary = ' '.join(summary_range_list)
    except Exception as e:
        print(f'Unable to convert CSV to Text File...\n\nERROR: {e}')
        input()

    # TODO: Look into adding another section that can parse out tables located on the page

    print("\nProcessing Complete!\n")

    # =============================================================================

    # DEBUGGING 
    # input(content.head())
    # input('\n'+summary)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# =============================================================================

# *** Longer Processing ***
# subprocess.run(['powershell.exe','clear-host; write-host "=== AI SUMMARY ===\n"; ollama','run','tinyllama',f'Give detailed summary of this article, and provide additional information if possible: "{summary}"'])

# *** Shorter Processing ***
subprocess.run(['powershell.exe','clear-host; write-host "=== AI SUMMARY ===\n"; ollama','run','tinyllama',f'Summarize this article: "{summary}"'])


