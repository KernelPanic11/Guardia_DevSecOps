###############################################
# Flask : Micro serveur web
# render_template_string : Afficher du HTML depuis Python
# jsonify : Traduction de dictionnaire Python en JSON pour nos navigateurs
# requests : Pour interagir avec les APIs
###############################################

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


# Page Principale
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/catfacts")
def page_catfacts():
    return render_template("catfacts.html")

@app.route("/catfacts/facts")
def get_catfacts():
    apiAnswer = requests.get("https://catfact.ninja/fact")
    data = apiAnswer.json()
    return data


@app.route("/pokeapi")
def page_pokeapi():
    return render_template("pokeapi.html")

@app.route("/pokeapi/getPokemon")
def get_pokemon():
    name = requests.args.get("name", "pikachu").lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    apiAnswer = requests.get(url)

    if apiAnswer.status_code != 200:
        return "Error : Pokemon not found"
    
    # Transforme en dictionnaire Python
    data = apiAnswer.json()

    stats = {
        "hp": data["stats"][0]["base_stat"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"]
    }

    sprite = data["sprites"]["front_default"]
    return jsonify({"stats": stats, "sprite": sprite, "name": name.capitalize()})




# Sécurité si importe de ce fichier dans un autre
# if __name__ == __main__ : 
app.run(debug=True)
