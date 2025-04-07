import sqlite3

from werkzeug.security import generate_password_hash, check_password_hash


def init_db():
    conn = sqlite3.connect('data/base.sqlite')
    curseur = conn.cursor()
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            mot_de_passe TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def ajouter_utilisateur(nom, prenom, email, mot_de_passe):
    conn = sqlite3.connect('data/base.sqlite')
    curseur = conn.cursor()
    hachage_mot_de_passe = generate_password_hash(mot_de_passe)
    curseur.execute(
        'INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe) VALUES (?, ?, ?, ?)',
        (nom, prenom, email, hachage_mot_de_passe)
    )
    conn.commit()
    conn.close()


def verifier_utilisateur(email, mot_de_passe):
    conn = sqlite3.connect('data/base.sqlite')
    curseur = conn.cursor()
    curseur.execute('SELECT mot_de_passe FROM utilisateurs WHERE email = ?', (email,))
    resultat = curseur.fetchone()
    conn.close()
    if resultat is None:
        return False
    mot_de_passe_hache = resultat[0]
    return check_password_hash(mot_de_passe_hache, mot_de_passe)
