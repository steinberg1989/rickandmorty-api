from flask import Flask, render_template_string
import requests

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; }
        .character { margin: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 8px; width: 200px; }
        img { width: 100%; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>Rick and Morty Characters</h1>
    <div class="container">
        {% for character in characters %}
        <div class="character">
            <h3>{{ character.name }}</h3>
            <p>Location: {{ character.location }}</p>
            <img src="{{ character.image }}" alt="{{ character.name }}">
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return '<h1>Rick and Morty API</h1><p>Visit <a href="/docs">/docs</a> for API documentation.</p>'

@app.route('/healthcheck')
def healthcheck():
    return {"status": "OK"}, 200

@app.route("/")
def get_characters():
    url = "https://rickandmortyapi.com/api/character/?species=Human&status=Alive"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        characters = [
            {"name": c["name"], "location": c["location"]["name"], "image": c["image"]}
            for c in data["results"]
        ]
        return render_template_string(TEMPLATE, characters=characters)
    else:
        return "<h1>Failed to load data</h1>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
