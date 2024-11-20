from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_string = request.form['inputString']
    action = request.form['action']  # Check which button was clicked

    if action == "2015_P1":
        # Perform the bracket difference calculation
        open_count = 0
        close_count = 0
        for char in input_string:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
            if close_count > open_count:
                result = f"Sum at imbalance: {open_count + close_count}"
                break
        else:
            result = f"Difference: {open_count - close_count} (Open - Close)"

    elif action == "2015_P2.1":
        # Perform a simple count of all parentheses
        total_count = input_string.count('(') + input_string.count(')')
        result = f"Total parentheses count: {total_count}"

    elif action == "2015_P2.2":
        # Split the input into lines
        lines = input_string.strip().splitlines()
        total_surface_area = 0

        # Process each line to calculate the required surface area
        for line in lines:
            # Split the line into dimensions: height, length, width
            dimensions = line.split('x')
            if len(dimensions) != 3:
                continue  # Skip if the line doesn't have exactly 3 values

            # Convert each dimension to an integer
            height, length, width = map(int, dimensions)

            # Calculate surface areas for each side
            twoheight = height + height
            twolength = length + length
            twowidth = width + width

            # Calculate the total area for this box
            bow = height * width * length

            # Add the smallest area as extra
            wrap = min(twoheight+twolength, twolength+twowidth, twowidth+twoheight) 

            # Add to the total surface area
            total_surface_area += wrap + bow

        # Set the result to the total calculated surface area
        result = f"Total Surface Area: {total_surface_area}"
        
    elif action == "2015_P3.1":

        updown = 0
        leftright = 0

        positions = []
        positions.append ((updown, leftright))

        for char in input_string:
            if char == '^':
                updown += 1
            elif char == 'v':
                updown -= 1
            elif char == '>':
                leftright += 1
            elif char == '<':
                leftright -= 1

            if (updown, leftright) not in positions:
               positions.append ((updown, leftright)) 

        numberOfHouses = len(positions)
        result = f"Number of houses: {numberOfHouses}"

    else:
        # Default case if the action is unrecognized
        result = "Invalid action or input."

    return result  # Always return a string result
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
