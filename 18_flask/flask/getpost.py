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


if __name__ == '__main__':   # entry point of the application
    app.run(debug=True)  # starts the Flask development server with debug mode enabled
    
    