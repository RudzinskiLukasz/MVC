from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Film
from app.forms import FilmForm

@app.route('/')
def index():
    filmy = Film.query.all()
    return render_template('list.html', filmy=filmy)

@app.route('/add_edit', methods=['GET', 'POST'])
def add_edit():
    form = FilmForm()
    if form.validate_on_submit():
        nowy_film = Film(
            tytul=form.tytul.data,
            rezyser=form.rezyser.data,
            ocena=form.ocena.data
        )
        db.session.add(nowy_film)
        db.session.commit()
        flash('Film został dodany!', 'success')
        return redirect(url_for('index'))
    return render_template('add_edit.html', form=form)

@app.route('/film/<int:film_id>/edytuj', methods=['GET', 'POST'])
def edytuj_film(film_id):
    film = Film.query.get_or_404(film_id)
    form = FilmForm(obj=film)
    if form.validate_on_submit():
        form.populate_obj(film)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_edit.html', form=form, action="Edytuj")

@app.route('/film/<int:film_id>/usun', methods=['POST'])
def usun_film(film_id):
    film = Film.query.get_or_404(film_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/film/<int:film_id>')
def szczegoly(film_id):
    film = Film.query.get_or_404(film_id)
    return render_template('details.html', film=film)
