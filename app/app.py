from flask import Flask, render_template, request, jsonify
from app.AOC_2015 import (
    p1_1, p1_2, p2_1, p2_2,
    p3_1, p3_2, p4_1, p4_2,
    p5_1, p5_2,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('aoc2015.html')

@app.route('/aoc2015_solve', methods=['POST'])
@login_required
def aoc2015_solve():
    data = request.get_json()
    input_string = data.get('inputString', '')
    action = data.get('action', '')

    try:
        if action == "P1.1":
            result = p1_1.calculate(input_string)
        elif action == "P1.2":
            result = p1_2.calculate(input_string)
        elif action == "P2.1":
            result = p2_1.calculate(input_string)
        elif action == "P2.2":
            result = p2_2.calculate(input_string)
        elif action == "P3.1":
            result = p3_1.calculate(input_string)
        elif action == "P3.2":
            result = p3_2.calculate(input_string)
        elif action == "P4.1":
            result = p4_1.calculate(input_string)
        elif action == "P4.2":
            result = p4_2.calculate(input_string)
        elif action == "P5.1":
            result = p5_1.calculate(input_string)
        elif action == "P5.2":
            result = p5_2.calculate(input_string)
        else:
            result = "Invalid action or input."
    except Exception as e:
        result = f"An error occurred: {str(e)}"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
