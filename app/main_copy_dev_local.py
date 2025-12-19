###############################################
# Flask : Micro serveur web
# render_template_string : Afficher du HTML depuis Python
# jsonify : Traduction de dictionnaire Python en JSON pour nos navigateurs
# requests : Pour interagir avec les APIs
###############################################

import requests

def Home():
    return render_template("index.html") # retourne le body HTTP de type HTML

#----------------------------------------------------------------------------------------------------------------


def Catfact_home():
    return render_template("catfacts.html")



def Show_catfact():
    maRequestCatfact = requests.get("https://catfact.ninja/fact")
    maRequestCatfact = maRequestCatfact.json()
    return maRequestCatfact

#---------------------------------------------------------------------------



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






















# def PokeHome():
#     return render_template("pokeapi.html")


# def GetPokeInfo():
#     pokeRequests = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
#     pokeJSON = pokeRequests.json()

#     # print(f"pokeJSON = {pokeJSON}")

#     pokeName = pokeJSON["name"]
#     pokeSprite = pokeJSON["sprites"]["front_default"]

#     pokeType = pokeJSON["types"][0]["type"]["name"]

# #   # Pour chaque stat dans le JSON du pokemon, afficher les valeurs de chaque stats (et selectionner avec [...][...])
#     pokeStats = {}
#     for stat in pokeJSON["stats"]:
#         # print(f"stat = {stat}, il est de type {type(stat)}")
#         print(f"{stat["stat"]["name"]} = {stat["base_stat"]}")
#         pokeStats[stat["stat"]["name"]] = stat["base_stat"]




#     print(f"Le nom du pokemon est {pokeName}")
#     print(f"Le sprite de {pokeName} est {pokeSprite}")
#     print(f"Le type de {pokeName} est {pokeType}")















# def GetPokeInfo():
#     pokeName = ""
#     pokeRequests = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
#     pokeJSON = pokeRequests.json() # Le JSON entier, à parcourir
#     print(f"Voici le resultat brut du JSON : {pokeJSON} \n \n")

#     pokeName = pokeJSON["species"]["name"]

#     pokeSprite = pokeJSON["sprites"]["front_default"]
#     print(f"La valeur du sprite est : {pokeSprite}, il est de type : {type(pokeSprite)}")

#     pokeSpriteShiny = pokeJSON["sprites"]["front_shiny"]

#     pokeTypes = {}
#     for typeDuPokemon in pokeJSON["types"]:
#         pokeTypes = typeDuPokemon["type"]["name"] # recheck ça pour les multi-types
    
#     # Pour chaque stat dans le JSON du pokemon, afficher les valeurs de chaque stats (et selectionner avec [...][...])
#     pokeStats = {}
#     for stat in pokeJSON["stats"]:
#         # print(f"stat = {stat}, il est de type {type(stat)}")
#         print(f"{stat["stat"]["name"]} = {stat["base_stat"]}")
#         pokeStats[stat["stat"]["name"]] = stat["base_stat"]
#         # pokeStats = {
#         #     "Nom": stat["stat"]["name"],
#         #     "Valeur": stat["base_stat"]
#         # }


#     dictionnaireDeRetour = {
#         "pokeName": pokeName,
#         "pokeSprite": pokeSprite,
#         # Afficher le sprtie de chaque gen ? Ou plutot front_default + front_shiny
#         "pokeSpriteShiny": pokeSpriteShiny,
#         # Afficher la descr -> clef genera
#         "pokeTypes" : pokeTypes,
#         "pokeStat" : pokeStats
#     }

#     print(f"Le dictionnaire de retour contient : {dictionnaireDeRetour}")



ShowPokemon()








