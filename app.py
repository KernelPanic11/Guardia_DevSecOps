###############################################
# Flask : Micro serveur web
# render_template_string : Afficher du HTML depuis Python
# jsonify : 
# requests : Pour interagir avec les APIs
###############################################

from flask import Flask, render_template_string
import requests

app = Flask(__name__)


# Page Principale
@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cat Facts</title>
    </head>
    <body>
        <h1>Cat Facts 😺</h1>
        <button onclick="getFact()">Obtenir un fait !</button>
        <p id="fact"></p>

        <script>
            function getFact() {
                fetch('/fact')
                .then(apiAnswer => apiAnswer.json())
                .then(data => {
                    document.getElementById('fact').innerText = data.fact;
                })
                .catch(err => console.error(err));
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/fact")
def fact():
    apiAnswer = requests.get("https://catfact.ninja/fact")
    data = apiAnswer.json()
    return data


# Sécurité si importe de ce fichier dans un autre
if __name__ == __name__ : 
    app.run(debug=True)
