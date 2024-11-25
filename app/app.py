from flask import Flask, render_template, request, jsonify
from app.actions import (
    y2015_p1_1,
    y2015_p1_2,
    y2015_p2_1,
    y2015_p2_2,
    y2015_p3_1,
    y2015_p3_2,
    y2015_p4_1,
    y2015_p4_2,
    y2015_p5_1,
    y2015_p5_2,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # Receive JSON data from the front end
    input_string = data.get('inputString', '')
    action = data.get('action', '')

    # Route to the appropriate function based on the action
    try:
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
        elif action == "2015_P5.1":
            result = y2015_p5_1.calculate(input_string)
        elif action == "2015_P5.2":
            result = y2015_p5_2.calculate(input_string)
        else:
            result = "Invalid action or input."
    except Exception as e:
        result = f"An error occurred: {str(e)}"

    # Return the result as plain text
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
