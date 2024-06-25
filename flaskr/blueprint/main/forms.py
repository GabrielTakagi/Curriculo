from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class contactForm(FlaskForm):
     nome = StringField('Mome', validators=[ Length(max=60, min=1)], )
     email = EmailField('Email', validators=[ Email(), Length(max=80, min=1)])
     mensagem = TextAreaField('Mensagem', validators=[ Length(max=350, min=1)], render_kw={"rows": 8})
     enviar = SubmitField('Enviar')
