from my_app import app

app.config.from_pyfile('config.py')
#app.config.from_object('configuration.ProductionConfig')
print(app.config['DEBUG'])

app.run()#debug=True 
#app.config['debug']=True   #Sirven para recargar automaticamente los cambios cuando se guardan de forma automatica
#app.debug=True