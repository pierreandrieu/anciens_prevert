from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class FormulaireInscription(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prénom', validators=[DataRequired()])
    email = StringField('Adresse e-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm = PasswordField('Confirmez le mot de passe', validators=[
        DataRequired(),
        EqualTo('password', message='Les mots de passe doivent correspondre.')
    ])
    envoyer = SubmitField("S'inscrire")


class FormulaireConnexion(FlaskForm):
    email = StringField('Adresse e-mail', validators=[DataRequired(), Email()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    envoyer = SubmitField('Se connecter')
