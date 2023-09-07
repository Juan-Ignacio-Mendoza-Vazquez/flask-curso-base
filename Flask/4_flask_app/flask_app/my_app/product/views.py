#from my_app import app
from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from werkzeug.exceptions import abort
from my_app import db
from my_app.product.model.products import PRODUCTS
from my_app.product.model.product import Product
from sqlalchemy.sql.expression import not_, or_

product=Blueprint('product',__name__)

@product.route('/')
@product.route('/home')
def index():
    return render_template('product/index.html', products=Product.query.all())

@product.route('/product/<int:id>')
def show(id):
    product=Product.query.get_or_404(id)
#    if not product:
#        abort(404)

    return render_template('product/show.html',product=product)

@product.route('/product-create')
def create():
    print(get_flashed_messages())
    return render_template('product/create.html')

@product.route('/product-insert', methods=['POST'])
def insert():
    p=Product(request.form['name'], request.form['price'])
    db.session.add(p)
    db.session.commit()
    flash("Producto creado con exito")
    return redirect(url_for('product.create'))

@product.route('/test')
def test():
    #p = Product.query.all()
    #p = Product.query.order_by(Product.id).limit(2)
    #p = Product.query.limit(2).first()
    #p = Product.query.order_by(Product.id).limit(2).all()
    #p = Product.query.order_by(Product.id.desc()).limit(2).all()
    #p = Product.query.get({"id":1})
    #p = Product.query.filter_by(name="Producto 1").all()
    #p = Product.query.filter(Product.id > 1).all()
    #p = Product.query.filter_by(name="Producto 1", id = 1).all()
    #p = Product.query.filter(Product.name.like('P%')).all()
    #p = Product.query.filter(not_(Product.id > 1)).all()
    #p = Product.query.filter(or_(Product.id > 1, Product.name=="Producto 1")).all()
    #print(p)
    
    #Insertar Registros
    #p=Product("Producto 5",60.8)
    #db.session.add(p)
    #db.session.commit()
    #Product.add(p)
    
    #Actualizar registros
    #p=Product.query.filter_by(name="Producto 1", id=1).first()
    #p.name = "UP1"
    #db.session.add(p)
    #db.session.commit()
    
    #Borrar registros
    #p=Product.query.filter_by(id=1).first()
    #db.session.delete(p)
    #db.session.commit()
    return "Flask"

@product.route('/filter/<int:id>')
def filter(id):
    product=PRODUCTS.get(id)
    return render_template('product/filter.html', product=product)

@product.app_template_filter('iva')
def iva_filter(product):
    if product['price']:
        return product['price'] * 0.20 + product['price']
    return 'Sin Precio'