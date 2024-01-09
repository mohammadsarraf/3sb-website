from flask import Flask, render_template
from test import get_cell_value, comms, types

app = Flask(__name__)

@app.route('/')
def home():
    result = get_cell_value("np", types, comms)  # Call your function
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
