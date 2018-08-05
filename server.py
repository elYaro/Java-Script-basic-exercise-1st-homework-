from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/templates/index.html')
def index():
    return render_template('index.html')


@app.route('/templates/line.html')
def line():
     return render_template('line.html')

@app.route('/templates/circle.html')
def circle():
     return render_template('circle.html')
     
@app.route('/templates/square.html')
def square():
     return render_template('square.html')     

@app.route('/templates/rectangle.html')
def rectangle():
     return render_template('rectangle.html')     

@app.route('/templates/parallelogram.html')
def parallelogram():
     return render_template('parallelogram.html')   

@app.route('/templates/trapezium.html')
def trapezium():
     return render_template('trapezium.html')   

@app.route('/templates/ellipse.html')
def ellipse():
     return render_template('ellipse.html')   







if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)



  
 