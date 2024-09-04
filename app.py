import threading
import webbrowser
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return ("you are underweight - eat more!", "too-thin")
    elif bmi < 25:
        return ("you have normal weight - keep on going!", "normal")
    else:
        return ("you are overweight - eat less and move more!", "too-fat")

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    cat = None
    classy = None
    if request.method == 'POST':
        height = float(request.form['height-m'])
        weight = float(request.form['weight-kg'])
        bmi = round(weight / (height/100)**2, 2)
        cat, classy = categorize_bmi(bmi)
    
    # Render the template
    return render_template('index.html', bmi=bmi, cat=cat, classy=classy)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run(debug=True, use_reloader=False)