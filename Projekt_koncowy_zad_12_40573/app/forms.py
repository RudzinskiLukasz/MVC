from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class FilmForm(FlaskForm):
    tytul = StringField('Tytuł', validators=[DataRequired()])
    rezyser = StringField('Reżyser', validators=[DataRequired()])
    ocena = FloatField('Ocena', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Zapisz')
