def calculate(input_string):
    updown = 0
    leftright = 0

    positions = []
    positions.append((updown, leftright))

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
            positions.append((updown, leftright))

    number_of_houses = len(positions)
    return f"Number of houses: {number_of_houses}"
