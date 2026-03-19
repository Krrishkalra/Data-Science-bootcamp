# Building URL dynamically
# jinja2 template
# variable rule

from flask import Flask, render_template, request

#it creates an instance of the Flask class, 
# which will be your WSGI application.

#WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")  # this function will be called when the root URL is accessed


@app.route("/index",methods = ['GET'])
def index():
    return "This is the index page."  # this function will be called when the /index URL is accessed


@app.route('/form',methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"  # this function will be called when the /form URL is accessed with a POST request
    return render_template('form.html')

        
@app.route('/submit',methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"  # this function will be called when the /form URL is accessed with a POST request
    return render_template('form.html')


#variable rule
@app.route("/success/<int:score>")
def success(score):
    return "Your marks are "+ str(score)
    

# dynamic url using jinja2 template
@app.route("/result/<int:score>")
def result(score):
    res = ""
    if score >=50:
        res = "'passed'"
    else:
        res = "'failed'"
    
    return render_template("result1.html", results = res)

    
@app.route("/resultscr/<int:score>")
def resultscr(score):
    res = ""
    if score >=50:
        res = "'passed'"
    else:
        res = "'failed'"
    
    exp = {'score': score, 'result': res}
    return render_template("resultscr.html", results = exp)

        
@app.route("/resultif/<int:score>")
def resultif(score):
    
    return render_template("result.html", results = score)

    
if __name__ == '__main__':   # entry point of the application
    app.run(debug=True)  # starts the Flask development server with debug mode enabled
    
    