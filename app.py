from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:Pass123*@3.145.80.6:3306/bd'
db = SQLAlchemy(app)

# Definir tabla
class Compras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))
    cantidad = db.Column(db.String(100))

class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))
    cantidad = db.Column(db.String(100))

@app.route('/')
def mostrar_datos():
    # Consultar los datos de la base de datos y ordenar por la columna id
    compras = Compras.query.order_by(Compras.id).all()
    ventas = Ventas.query.order_by(Ventas.id).all()
    return render_template('index.html', compras=compras, ventas=ventas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)