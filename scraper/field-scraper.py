from bs4 import BeautifulSoup
import requests
import dinosaurs as dino_names

fields_collection = []
model = 'https://www.nhm.ac.uk/discover/dino-directory/'
for name in dino_names.endpoints:
    fields = {
        "name": "",
        "diet": "",
        "era": "",
        "found": "",
        "avg_weight_kg": "",
        "avg_length_m": "",
        "movement": ""
    }
    html = requests.get(model + name + '.html').text
    parsed_html = BeautifulSoup(html, features='html.parser')
    container1 = parsed_html.find('dl', 'dinosaur--description dinosaur--list')
    container2 = parsed_html.find('dl', 'dinosaur--info dinosaur--list')
    fields['avg_length_m'] = 'xx'
    print(fields)
    print("FUCK YOU CHARLIE")
    print(container2)
