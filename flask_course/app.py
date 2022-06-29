# from flask import Flask 

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<h1> Hello world </h1>"

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template 

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
    # app.run(debug=True)


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     vardai = ['Jonas', 'Antanas', 'Petras']
#     return render_template("index.html", sarasas=vardai)


# if __name__ == "__main__":
#     app.run()


# from flask import Flask, request, render_template
# app = Flask(__name__)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         vardas = request.form['vardas']
#         return render_template("greetings.html", vardas=vardas)
#     else:
#         return render_template("login.html")


# if __name__ == "__main__":
#     app.run()
    


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     vardai = ['Jonas', 'Antanas', 'Petras']
#     return render_template("index.html", sarasas=vardai)

# if __name__ == "__main__":
#     app.run()

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# pilnas kelias iki šio failo.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# neseksime kiekvienos modifikacijos
db = SQLAlchemy(app)
# sukuriame duomenų bazės objektą
# sukurkime modelį užklausos formai, kuris sukurs duomenų bazėje lentelę


class Message(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f'{self.name} - {self.email}'
