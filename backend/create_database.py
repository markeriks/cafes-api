from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///kohvikud.sqlite")
Base = declarative_base()
Session = sessionmaker(engine)

class Sookla(Base):
    __tablename__ = "SOOKLA"
    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Location = Column(String, nullable=False)
    Teenusepakkuja = Column(String, nullable=False)
    time_open = Column(String, nullable=False)
    time_closed = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id":self.ID,
            "name": self.Name,
            "location": self.Location,
            "teenusepakkuja": self.Teenusepakkuja,
            "time_open": self.time_open,
            "time_closed": self.time_closed,
        }

Base.metadata.create_all(engine)