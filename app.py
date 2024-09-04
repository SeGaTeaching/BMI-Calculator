from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        height = request.form['height-m']
        weight = request.form['weight-kg']
        bmi = round(weight / height**2, 2)
    
    # Render the template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)