from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrace")
def registrace():
    name = request.args.get("name")
    c_count = request.args.get("count")

    if c_count != "" and c_count != None:
        if int(c_count) > 17:
            return render_template("registrace.html", jinja_count=c_count, jinja_name=name)

    return render_template("registrace.html")

if __name__ == "__main__":
    app.run(debug=True)