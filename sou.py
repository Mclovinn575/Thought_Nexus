import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os

def Parse_Page(url):
    # Attempt to connect to site
    os.system('cls')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def Get_Title(page_data):
    title = page_data.find('title').text
    return title

def Get_Topics(page_data):
    topics = {}
    topic = ''
    data = page_data.find_all(['h1','h2','h3','h4','h5','h6','p'])
    # print(data)
    for tag in data:
        # TOPIC
        if tag.name.startswith('h'):
            topic = tag.text.strip()
            topics[topic] = []
        # PARAGRAPHS
        elif topic and tag.name == 'p':
            topics[topic].append(tag.text.strip())
    for title in topics.keys():
        print(title)
    return topics

def Get_Body(topics, target_topic):
    for paragraphs in topics[target_topic]:
        print(paragraphs)
        print('')
    input('\nPress ENTER to continue...')

user_topic = 'N/A'


base_url = "https://en.wikipedia.org/wiki"

if __name__ == "__main__":
    while True:
        menu = f"""
============================================================================================================
Current Search: {user_topic}

1.) Enter Search

2.) Get Information

Q.) Exit

============================================================================================================
        """
        # Run Main Code
        os.system('cls')
        print(menu)
        menu_choice = input("\n>>: ").lower()
        if menu_choice == '1':
            user_topic = input('Enter Topic: ')
        elif menu_choice == '2':
            page_data = Parse_Page(url=f'{base_url}/{user_topic}')
            while True:
                os.system('cls')
                print('TOPICS:\n')
                topics = Get_Topics(page_data)
                target_body = input('\nSelect Topic: ')
                if target_body in topics:
                    Get_Body(topics, target_body)
                elif target_body == 'q':
                    break
        elif menu_choice == 'q':
            print("\nEXITING...")
            break
        else:
            print("\nINCORRECT CHOICE. PLEASE TRY AGAIN.")
            input("Press ENTER to continue...")





