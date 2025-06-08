# seed.py

from app import db
from app.models import Film
from app import app

# Lista przykładowych filmów
filmy_80s = [
    {"tytul": "Blade Runner", "rezyser": "Ridley Scott", "ocena": 9.0},
    {"tytul": "Back to the Future", "rezyser": "Robert Zemeckis", "ocena": 8.7},
    {"tytul": "The Shining", "rezyser": "Stanley Kubrick", "ocena": 8.4},
    {"tytul": "The Empire Strikes Back", "rezyser": "Irvin Kershner", "ocena": 8.8},
    {"tytul": "Die Hard", "rezyser": "John McTiernan", "ocena": 8.2},
    {"tytul": "Scarface", "rezyser": "Brian De Palma", "ocena": 8.3},
    {"tytul": "Aliens", "rezyser": "James Cameron", "ocena": 8.4},
    {"tytul": "The Terminator", "rezyser": "James Cameron", "ocena": 8.0},
    {"tytul": "Raging Bull", "rezyser": "Martin Scorsese", "ocena": 8.2},
    {"tytul": "E.T. the Extra-Terrestrial", "rezyser": "Steven Spielberg", "ocena": 7.9}
]

# Dodaj dane do bazy
with app.app_context():
    db.create_all()  # Upewnij się, że tabela istnieje
    db.session.query(Film).delete()  # Czyść bazę przed seedowaniem (opcjonalne)
    for film in filmy_80s:
        db.session.add(Film(**film))
    db.session.commit()
    print(" Baza danych uzupełniona filmami.")
