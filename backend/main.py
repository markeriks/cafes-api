from doctest import debug

from flask import Flask, request, jsonify
from create_database import engine, Sookla
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

SessionLocal = sessionmaker(engine, autocommit=False)

# Pärida kõiki kohvikuid andmebaasist (GET)
@app.route("/cafes", methods=["GET"])
def get_all_cafes():
    database = SessionLocal()
    cafes = database.query(Sookla).all()
    database.close()
    response = jsonify([cafe.to_dict() for cafe in cafes])
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route("/cafes/<int:cafe_id>", methods=["GET"])
def get_single_cafe(cafe_id):
    database = SessionLocal()
    cafe = database.query(Sookla).filter(Sookla.ID == cafe_id).first()
    database.close()
    if cafe:
        response = jsonify(cafe.to_dict())
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

# Pärida kohvikuid avamisaja järgi (GET)
@app.route("/cafes/open/<opentime>", methods=["GET"])
def get_cafes_by_open_time(opentime: str):
    database = SessionLocal()
    cafes = database.query(Sookla).filter(Sookla.time_open == opentime).all()
    database.close()
    return jsonify([cafe.to_dict() for cafe in cafes])

# Lisada uusi kohvikuid (POST)
@app.route("/cafes/post", methods=["POST"])
def add_cafe():
    data = request.get_json()
    database = SessionLocal()
    new_cafe = Sookla(
        Name = data["name"],
        Location = data["location"],
        Teenusepakkuja = data["teenusepakkuja"],
        time_open = data["time_open"],
        time_closed = data["time_closed"]
    )
    database.add(new_cafe)
    database.commit()
    database.close()
    return jsonify(new_cafe.__dict__)

# Muuta kohviku andmeid (PUT)
@app.route("/cafes/update/<int:cafe_id>", methods=["PUT"])
def update_cafe(cafe_id):
    data = request.get_json()
    database = SessionLocal()
    cafe = database.query(Sookla).filter(Sookla.ID == cafe_id).first()
    if not cafe:
        database.close()
        return {"message": "Cafe not found"}, 404
    cafe.Name = data["name"]
    cafe.Location = data["location"]
    cafe.Teenusepakkuja = data["teenusepakkuja"]
    cafe.time_open = data["time_open"]
    cafe.time_closed = data["time_closed"]

    database.commit()
    database.close()


# Kustutada kohvik andmebaasist (DELETE)
@app.route("/cafes/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    database = SessionLocal()
    cafe = database.query(Sookla).filter(Sookla.ID == cafe_id).first()
    if not cafe:
        database.close()
        return {"message": "Cafe not found"}, 404
    database.delete(cafe)
    database.commit()
    database.close()
    return {"message": "Cafe deleted"}, 200

if __name__ == "__main__":
    app.run(debug=True)


