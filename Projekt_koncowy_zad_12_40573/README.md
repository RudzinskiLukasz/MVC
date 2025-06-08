# Katalog kolekcji filmów

## Spis treści
1. [Opis projektu](#opis-projektu)  
2. [Funkcjonalności](#funkcjonalności)  
3. [Technologie](#technologie)  
4. [Instrukcja uruchomienia](#instrukcja-uruchomienia)  
5. [Plik seed](#plik-seed)  

---

## Opis projektu
Projekt to prosty katalog filmów z możliwością wyświetlania listy filmów, dodawania nowych pozycji, edycji istniejących oraz usuwania. Aplikacja oparta jest na wzorcu MVC, wykorzystując Flask jako framework webowy oraz SQLite jako bazę danych.

---

## Funkcjonalności
- Wyświetlanie listy filmów  
- Dodawanie nowego filmu poprzez formularz  
- Edycja danych filmu  
- Usuwanie filmu z katalogu  
- Walidacja formularzy po stronie serwera (WTForms)  
- Przechowywanie danych w lokalnej bazie SQLite  

---

## Technologie
- Python 3.13.3
- Flask 
- Flask-WTForms
- SQLite
- HTML/CSS (Bootstrap do stylizacji)  

---

## Instrukcja uruchomienia

1. **Klonowanie repo**  

git clone <URL_REPOZYTORIUM>
cd <nazwa_folderu>

2. **Utworzenie środowiska wirtualnego**

Dla windowsa:

python -m venv venv
venv\Scripts\activate

dla linuxa:
python3 -m venv venv
source/venv/bin/activate

3. **Instalacja wymaganych pakietów**

pip install -r requirements.txt

4. **Uruchomienie aplikacji**

flask run

5. **Dostęp z przeglądarki**

http://127.0.0.1:5000

## Plik seed

Inicjalizuje baze danych z przykładowymi filmami.
ŚRODOWISKO MUSI BYĆ AKTYWNE

**Uruchomienie**

python seed.py

Skrypt utworzy bazę danych i doda do niej rekordy.
Po wykonatniu powyższego korzystamy z komendy: flask run
