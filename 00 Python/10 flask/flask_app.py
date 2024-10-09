from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/bye")
def bye(): 
    return render_template("bye.html")

@app.route("/form")
def form():
    name = request.args.get("name", default="_____")
    input_class = request.args.get("class", default="_____")
    message = request.args.get("message", default="_____")
    return render_template("form.html", name=name, form_class=input_class, message=message)





if __name__ == "__main__":
    app.run(debug=True)