from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
from practico_06.capa_negocio import NegocioSocio
from practico_05.ejercicio_01 import Socio

# FALTA HACER MEJOR LA BARRA DE NAVEGACION Y HACER LAS ALERTAS DE LAS EXCEPCIONES

app = Flask(__name__, template_folder='view/templates/', static_folder='view/static/')

app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    socios = NegocioSocio().todos()
    return render_template('index.html', socios = socios)

@app.route('/alta/')
def alta():
    return render_template('add.html')

@app.route('/add/', methods = ['POST'])
def add():
    try:
        _dni = request.form['dni']
        _nombre = request.form['nombre']
        _apellido = request.form['apellido']
        NegocioSocio().alta(Socio(dni = _dni, nombre = _nombre, apellido = _apellido))
        flash('Socio agregado')
        return redirect(url_for('home'))
    except:
        return 'no saved'

@app.route('/delete/', methods = ['POST'])
def delete():
    try:
        _id = request.form['id']
        NegocioSocio().baja(_id)
        flash('Socio borrado')
        return redirect(url_for('home'))
    except:
        return 'no borrado'

@app.route('/delete/<id>')
def delete_btn(id):
    try:
        NegocioSocio().baja(id)
        return 'borrado'
    except:
        return 'no borrado'

@app.route('/modificar/<dni>')
def modificar_btn(dni):
    try:
        socio = NegocioSocio().buscar_dni(dni)
        return render_template('update.html', soc = socio)
    except:
        return 'no modificado'

@app.route('/update/<dni>', methods = ['POST'])
def update_btn(dni):
    try:
        _nombre = request.form['nombre']
        _apellido = request.form['apellido']
        NegocioSocio().modificacion(Socio(dni = dni, nombre = _nombre, apellido = _apellido))
        flash('Contacto actualizado')
        return redirect(url_for('home'))
    except:
        return 'no modificado'

# @app.route('/busqueda/')
# def busqueda():
#     return render_template('busqueda.html')

# @app.route('/busqueda/', methods = ['POST'])
# def buscar():
#     _dni = request.form['dni']
#     print(_dni)
#     socio = NegocioSocio().buscar_dni(_dni)
#     return render_template('search.html', soc = socio)

# @app.route('/modificar/')
# def modificar():
#     return render_template('update.html')

# @app.route('/update/', methods = ['POST'])
# def update():
#     try:
#         _dni = request.form['dni']
#         _nombre = request.form['nombre']
#         _apellido = request.form['apellido']
#         NegocioSocio().modificacion(Socio(dni = _dni, nombre = _nombre, apellido = _apellido))
#         return 'modificado'
#     except:
#         return 'no modificado'

if __name__ == '__main__':
    app.run(debug=True)