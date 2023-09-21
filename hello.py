from flask import Flask

# instaciamos Flask, tenemos que pasar un nombre de app

app = Flask(__name__)


@app.route('/')
def hola():
    return 'Hola, soy Flask. ¿Cómo te llamas?'


@app.route('/adios')
def adios():
    return 'Te dejo, que tengo hambre'


@app.route('/new')
def nueva():
    return 'Esta es una ruta nueva. Cuidado con los moradores de las arenas'
