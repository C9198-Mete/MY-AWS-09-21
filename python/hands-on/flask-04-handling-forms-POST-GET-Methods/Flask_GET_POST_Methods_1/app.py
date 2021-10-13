# Import Flask modules
from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)
# Create a function named `index` which uses template file named `index.html` 
# send three numbers as template variable to the app.py and assign route of no path ('/') 
@app.route('/')
def index():
    return render_template('index.html')

# calculate sum of them using inline function in app.py, then sent the result to the 
# "number.html" file and assign route of path ('/total'). 
# When the user comes directly "/total" path, "Since this is GET 
# request, Total hasn't been calculated" string returns to them with "number.html" file
@app.route('/total', methods=['GET', 'POST'])

# Add a statement to run the Flask application which can be debugged.

