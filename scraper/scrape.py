
# web scraping script to get all the dino names from the www.nhm.ac.uk

from bs4 import BeautifulSoup
import requests

# part 1: dinosaur names
# obtain the html file
html = requests.get(
    'https://www.nhm.ac.uk/discover/dino-directory/name/name-az-all.html').text

# parse the html file
parsed_html = BeautifulSoup(html, features='html.parser')

# isolate your tags to a list
dinos = parsed_html.find_all(
    'li', 'dinosaurfilter--dinosaur dinosaurfilter--all-list')

# isolate further
dino_names = []
for dinosaur in dinos:
    name = dinosaur.find(
        'p', 'dinosaurfilter--name dinosaurfilter--name-unhyphenated').get_text()
    dino_names.append(name.strip().lower())

# part 2: dinosaur fields
# url model for the field types
fields_collection = []
model = 'https://www.nhm.ac.uk/discover/dino-directory/'
for n in dino_names:
    fields = {
        "name": "",
        "diet": "",
        "era": "",
        "found": "",
        "avg_weight_kg": "",
        "avg_length_m": "",
        "movement": ""
    }
    link = model + n
    html2 = requests.get(link).text
    parsed_html2 = BeautifulSoup(html2, features='html.parser')
    container1 = parsed_html2.find('dl', 'dinosaur--description dinosaur--list')
    container2 = parsed_html2.find('dl', 'dinosaur--info dinosaur--list')
    fields['avg_length_m'] = 'xx'
    print(fields)
    print("FUCK YOU CHARLIE")
    print(container2)
    break
# profit
# print(dino_names)
