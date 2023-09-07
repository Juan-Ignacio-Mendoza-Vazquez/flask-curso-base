from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hola')
def hello_world():
    print(__name__)
    return '¡Hola mundo Flask! :)'
   
@app.route('/test')
def hello_world2():
    return '¡Hola mundo test! :o'
if __name__ == '__main__':
    app.run()
    
@app.route('/saludar/')
@app.route('/saludar/<hi>')
@app.route('/saludar/<hi>/<lang>')
def saludar(hi='Juan Ignacio',lang='es'):
    return '¡Hola '+hi+' '+lang+'!'

@app.route('/primer_html')
@app.route('/primer_html/<name>')
def primer_html(name='Juan Ignacio'):
    return '''
        <html>
            <body>
                <h1>Hola Flask</h1>
                <p>Hola %s
                <ul>
                    <li>item 1</li>
                    <li>item 2</li>
                </ul>
            </body>
        </html>
     ''' %name

@app.route('/static_file')
def static_file():
    return "<img src='"+url_for("static",filename="img/ako_riko.jpg")+"'>"
    #return "<img src='/static/img/ako_riko.jpg'>"
    
@app.route('/mi_primer_template')
@app.route('/mi_primer_template/<name>')
def mi_primer_template(name="Juan Ignacio"):
    return render_template('view.html',vname=name)

if __name__ == '__main__':
    app.run()