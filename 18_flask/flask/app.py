from flask import Flask

#it creates an instance of the Flask class, 
# which will be your WSGI application.

#WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to best Flask course!"  # this function will be called when the root URL is accessed

@app.route("/index")
def index():
    return "This is the index page."  # this function will be called when the /index URL is accessed


if __name__ == '__main__':   # entry point of the application
    app.run(debug=True)  # starts the Flask development server with debug mode enabled
    
    