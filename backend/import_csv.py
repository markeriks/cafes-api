import csv
from sqlalchemy.orm import sessionmaker
from create_database import engine, Sookla

Session = sessionmaker(engine)
connection = Session()

with open("Kohvikud.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        kohvik = Sookla(
            Name = row[0],
            Location = row[1],
            Teenusepakkuja = row[2],
            time_open = row[3],
            time_closed = row[4]
        )
        connection.add(kohvik)

connection.commit()
connection.close()