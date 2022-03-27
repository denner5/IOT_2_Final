from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #Navn på url 
@app.route('/home') 
def home(): 
    return render_template('home.html') 

@app.route('/side1')
def side1(): 
    return render_template('side1.html')   


@app.route('/datasheet') 
def datasheet(): 
    return render_template('datasheet.html') 


if __name__ == '__main__': 
    app.run() 
