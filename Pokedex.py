# Import necessary libraries
import requests
import json
from prettytable import PrettyTable
import os

os.system('cls')

# Function to parse and display Pokemon information
def display_pokemon_info(pokemon_data):
    table = PrettyTable()
    table.field_names = ["Name", "Type", "Abilities"]

    # Extract relevant information from the API response
    name = pokemon_data['name'].capitalize()
    types = ', '.join([t['type']['name'].capitalize() for t in pokemon_data['types']])
    abilities = ', '.join([a['ability']['name'].capitalize() for a in pokemon_data['abilities']])

    # Add data to the table
    table.add_row([name, types, abilities])

    # Display the table
    print(table)

# User input
pokemon = input("Enter Pokemon Name: ")
pokeURL = "https://pokeapi.co/api/v2/pokemon/"
lookup = pokeURL + pokemon
lookupResult = requests.request("get", lookup)
resultContent = lookupResult.content
rJson = json.loads(resultContent)

# Display Pokemon information
display_pokemon_info(rJson)
# look into looping this to ask if user would like to lookup multiple at once.

