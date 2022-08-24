from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		form_data = request.form
		return render_template('about.html', titre = 'blabla')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/form")
def form ():
	return render_template('form.html')

app.run(debug=True)

# import de l’objet Flask
# instantiation application
# association d’une route (URL) avec la fonction ‘home()’ et on renvoie une chaîne de caractères
# démarrage de l’application
