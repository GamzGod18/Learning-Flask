from  flask import Flask

app =Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/bacon')
def bacon():
    return '<h2>Hello Bacon</h2>'


if __name__ =="__main__":
    app.run(debug=True)








