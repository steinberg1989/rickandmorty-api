import requests
import csv

url = "https://rickandmortyapi.com/api/character/?species=Human&status=Alive&origin=Earth"
response = requests.get(url)
data = response.json()

if 'results' in data and data['results']:
    with open('characters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Location', 'Image'])

        for character in data['results']:
            name = character['name']
            location = character['location']['name']
            image = character['image']
            writer.writerow([name, location, image])
    print("CSV written successfully.")
else:
    print("No data found or incorrect query parameters.")
