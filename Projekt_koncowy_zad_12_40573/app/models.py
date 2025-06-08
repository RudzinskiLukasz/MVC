from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tytul = db.Column(db.String(100), nullable=False)
    rezyser = db.Column(db.String(100), nullable=False)
    ocena = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Film {self.tytul}>"
