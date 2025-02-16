import requests
import csv

url = "https://rickandmortyapi.com/api/character/?species=Human&status=Alive&origin=Earth"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open('characters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Location', 'Image'])

        for character in data['results']:
            name = character['name']
            location = character['location']['name']
            image = character['image']
            writer.writerow([name, location, image])

    print("Data written to characters.csv")
else:
    print(f"Failed to fetch data: {response.status_code}")
