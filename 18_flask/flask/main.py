from flask import Flask, render_template, request

#it creates an instance of the Flask class, 
# which will be your WSGI application.

#WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")  # this function will be called when the root URL is accessed

@app.route("/index")
def index():
    return "This is the index page."  # this function will be called when the /index URL is accessed



if __name__ == '__main__':   # entry point of the application
    app.run(debug=True)  # starts the Flask development server with debug mode enabled
    