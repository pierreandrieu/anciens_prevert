from flask import Flask, render_template, redirect, request, flash, session
from form import FormulaireInscription, FormulaireConnexion
from db import init_db, ajouter_utilisateur, verifier_utilisateur

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

init_db()


@app.route('/')
def accueil():
    return render_template('accueil.html')


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = FormulaireInscription()
    if form.validate_on_submit():
        ajouter_utilisateur(form.nom.data, form.prenom.data, form.email.data, form.password.data)
        return redirect('/')
    return render_template('inscription.html', form=form)


@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    form = FormulaireConnexion()
    if form.validate_on_submit():
        if verifier_utilisateur(form.email.data, form.mot_de_passe.data):
            session['email'] = form.email.data
            return redirect('/intranet_anciens')
        else:
            flash('Adresse e-mail ou mot de passe incorrect !')
    return render_template('connexion.html', form=form)


@app.route('/logout')
def logout():
    session.pop('email', None)
    flash("Vous avez été déconnecté.")
    return redirect('/')


@app.route('/intranet_anciens')
def intranet_anciens():
    return render_template('intranet_anciens.html')


if __name__ == '__main__':
    app.run(debug=True)
