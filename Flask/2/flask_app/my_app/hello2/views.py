from my_app import app

@app.route('/hello1')
def hello1():
    return 'Hola Mundo1'