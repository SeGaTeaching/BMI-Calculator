from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "you are underweight - eat more!"
    elif bmi < 25:
        return "you have normal weight - keep on going!"
    else:
        return "you are overweight - eat less and move more!"

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    cat = None
    if request.method == 'POST':
        height = float(request.form['height-m'])
        weight = float(request.form['weight-kg'])
        bmi = round(weight / (height/100)**2, 2)
        cat = categorize_bmi(bmi)
    
    # Render the template
    return render_template('index.html', bmi=bmi, cat=cat)

if __name__ == '__main__':
    app.run(debug=True)