
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


# profit
# print(dino_names)
