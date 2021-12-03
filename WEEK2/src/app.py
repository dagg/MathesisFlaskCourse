from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/index/")
@app.route("/")
@app.route("/<name>")
def root(name=None):
    return render_template("index.html", myname=name)




@app.route("/books/")
def books():
    
    with open("mybooks.json") as json_file:
        jdict = json.load(json_file)

    return render_template("books.html", jdict=jdict)


if __name__ == "__main__":
    app.run(debug=True)
