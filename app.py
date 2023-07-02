from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/elements.html')
def elements():  # put application's code here
    return render_template('elements.html')

@app.route('/About.html')
def About():  # put application's code here
    return render_template('About.html')

@app.route('/Popular Words.html')
def Popular():  # put application's code here
    return render_template('Popular Words.html')
@app.route('/pie_data.html')
def pie():  # put application's code here
    return render_template('pie_date.html')

@app.route('/pie.html')
def pie1():  # put application's code here
    return render_template('pie.html')


@app.route('/bin.html')
def bin():  # put application's code here
    return render_template('bar-polar-stack-radial.html')

@app.route('/Histogram.html')
def Histogram():  # put application's code here
    return render_template('Histogram.html')

@app.route('/search_data.html')
def search_data():  # put application's code here
    return render_template('search_data.html')

if __name__ == '__main__':
    app.run()
