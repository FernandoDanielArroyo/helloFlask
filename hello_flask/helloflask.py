from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
	return "<p>Bienvenue chez moi</p>"
app.run()

# import de l’objet Flask
# instantiation application
# association d’une route (URL) avec la fonction ‘home()’ et on renvoie une chaîne de caractères
# démarrage de l’application
