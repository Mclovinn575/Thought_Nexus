import requests
import json

pokeURL = "https://pokeapi.co/api/v2/pokemon/magikarp"
result = requests.get(pokeURL)
content = result.content
final = json.loads(content)
descriptionURL = final["species"]["url"]
descRes = requests.get(descriptionURL)
descontent = descRes.content
descfinal = json.loads(descontent)
entries = descfinal['flavor_text_entries']
textEntries = []
for entry in entries:
    if entry['language']['name'] == 'en':
        textEntries.append(entry['flavor_text'])
print(textEntries[3])
# Currently tested that this will hold pokemon descriptions in an array for later use.