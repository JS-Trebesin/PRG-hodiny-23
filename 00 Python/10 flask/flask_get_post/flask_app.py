from flask import Flask, render_template, request, redirect, url_for

# Vytvoření aplikace Flask
app = Flask(__name__)

# @ vytváří dekorátor, který nám upravuje funkce
# v případě flasku řešíme routování, když uživatel nezadá specifickou cestu (tzn. je tam samotné /)
# tak nás přesměruje na funkci hello
@app.route("/")
def hello():
    return render_template("index.html") # render_template vrátí stránku index.html ze složky template

@app.route("/bye")
def bye(): 
    return render_template("bye.html")

@app.route("/form")
def form():
    name = request.args.get("name") #request.args.get("něco") používáme pro metodu GET, text v .get odpovídá jménu z formuláře v html
    input_class = request.args.get("class")
    message = request.args.get("message")

    if name and message and input_class:
        return redirect(url_for("result", name=name, form_class=input_class, message=message)) # redirect s pomocí url_for nás přesměruje na stránku
    
    return render_template("form.html")

@app.route("/result")
def result():
    name = request.args.get("name", default="_____")
    input_class = request.args.get("form_class", default="_____")
    message = request.args.get("message", default="_____")
    return render_template("result.html", name=name, form_class=input_class, message=message) # první name odpovídá názvu proměnné v html, kterou jsme vytvořili pomocí jinja2 { name }, druhé name tomu, co za tuto proměnnou dosazujeme



if __name__ == "__main__":
    app.run(debug=True) #spouštění flaskové aplikace