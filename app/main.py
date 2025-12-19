###############################################
# Flask : Micro serveur web
# render_template_string : Afficher du HTML depuis Python
# jsonify : Traduction de dictionnaire Python en JSON pour nos navigateurs
# requests : Pour interagir avec les APIs
###############################################

import requests
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)



@app.route("/")
def Home():
    return render_template("index.html") # retourne le body HTTP de type HTML

#----------------------------------------------------------------------------------------------------------------

@app.route("/catfacts_guardia")
def Catfact_home():
    return render_template("catfacts.html")


@app.route("/catfacts_guardia/fact")
def Show_catfact():
    maRequestCatfact = requests.get("https://catfact.ninja/fact")
    maRequestCatfact = maRequestCatfact.json()
    return maRequestCatfact

# #----------------------------------------------------------------------------------------------------------------

@app.route("/pokeapi")
def PokeHome():
    return render_template("pokeapi.html")


@app.route("/pokeapi/getPokeInfo")
def ShowPokemon():
    pokeRequests = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    pokeJSON = pokeRequests.json()

    pokeName = pokeJSON["name"]
    pokeSprite = pokeJSON["sprites"]["front_default"]
    pokeType = pokeJSON["types"][0]["type"]["name"]

    dictionnaireDeStat = {}
    for clef_statistics in pokeJSON["stats"]:
        dictionnaireDeStat[clef_statistics["stat"]["name"]] = clef_statistics["base_stat"]

    dictionnaireFinal = {
        "name" : pokeName,
        "type" : pokeType,
        "sprite" : pokeSprite,
        "stats" : dictionnaireDeStat
    }

    return dictionnaireFinal











# @app.route("/pokeapi")
# def pokeapiHome():
#     return render_template("pokeapi.html")

# @app.route("/pokeapi/getpokemon")
# def getPokemon():
#     pokeName = request.args.get("name")
#     print(pokeName)
#     myPokeRequest = requests.get("https://pokeapi.co/api/v2/pokemon/{pokeName}")
#     print(myPokeRequest)
#     myPokeRequest = myPokeRequest.json()
#     return jsonify(myPokeRequest)






# #----------------------------------------------------------------------------------------------------------------

#app.run(debug=True, host="172.17.0.2")
app.run(debug=True)






# # OLD : 

# # import requests


# # try:
# #     r = requests.get('https://catfact.ninja/fact', timeout=5)
# #     r.raise_for_status()
# #     print("L'API repond !")

# #     data = r.json()
# #     print("Voici un fait sur les chats : ", data["fact"])

# # except requests.exceptions.RequestException as e:
# #     print("Probleme d'API... Code erreur : ", e)
# #     exit (1)
# # except ValueError as e:
# #     print("Probleme de décodage JSON... Code erreur : ", e)
# #     exit (1)



