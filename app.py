from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    
    # Render the template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)