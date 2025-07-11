from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

localhost_url = "http://127.0.0.1:5000/cafes"

@app.route("/")
def index():
    response = requests.get(localhost_url)
    cafes = response.json()
    return render_template("index.html", cafes = cafes)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        open_time = request.form["open_time"]
        response = requests.get(f"{localhost_url}/open/{open_time}")
        cafes = response.json()
        return render_template("search.html", cafes = cafes, open_time=open_time)
    return render_template("search.html")

@app.route("/add", methods=["POST"])
def add_cafe():
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "teenusepakkuja": request.form["teenusepakkuja"],
        "time_open": request.form["time_open"],
        "time_closed": request.form["time_closed"]
    }
    requests.post(f"{localhost_url}/post", json=data)
    return redirect(url_for("index"))

@app.route("/update/<int:cafe_id>", methods=["GET", "POST"])
def update_cafe(cafe_id):
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "location": request.form["location"],
            "teenusepakkuja": request.form["teenusepakkuja"],
            "time_open": request.form["time_open"],
            "time_closed": request.form["time_closed"]
        }
        requests.put(f"{localhost_url}/update/{cafe_id}", json=data)
        return redirect(url_for("index"))
    response = requests.get(f"{localhost_url}/{cafe_id}")
    cafe = response.json()
    return render_template('update.html', cafe=cafe)

@app.route("/delete/<int:cafe_id>", methods=["POST"])
def delete_cafe(cafe_id):
    requests.delete(f"{localhost_url}/delete/{cafe_id}")
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(port=5001)