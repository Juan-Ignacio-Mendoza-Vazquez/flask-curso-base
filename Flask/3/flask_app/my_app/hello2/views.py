#from my_app import app
from flask import Blueprint

hello2=Blueprint('hello2',__name__)

@hello2.route('/hello1')
def fhello2():
    return 'Hola Mundo1'