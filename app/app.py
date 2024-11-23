from flask import Flask, render_template, request
from app.actions import (
    y2015_p1_1,
    y2015_p1_2,
    y2015_p2_1,
    y2015_p2_2,
    y2015_p3_1,
    y2015_p3_2,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_string = request.form['inputString']
    action = request.form['action']  # Check which button was clicked

    # Route to the appropriate function based on action
    if action == "2015_P1.1":
        result = y2015_p1_1.calculate(input_string)
    elif action == "2015_P1.2":
        result = y2015_p1_2.calculate(input_string)
    elif action == "2015_P2.1":
        result = y2015_p2_1.calculate(input_string)
    elif action == "2015_P2.2":
        result = y2015_p2_2.calculate(input_string)
    elif action == "2015_P3.1":
        result = y2015_p3_1.calculate(input_string)
    elif action == "2015_P3.2":
        result = y2015_p3_2.calculate(input_string)
    elif action == "2015_P4.1":
        result = y2015_p4_1.calculate(input_string)
    elif action == "2015_P4.2":
        result = y2015_p4_2.calculate(input_string)
    else:
        result = "Invalid action or input."

    #print(f"DEBUG: Calculated result: {result}")  # Debugging the result value
    # return result  # Always return a string result
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
