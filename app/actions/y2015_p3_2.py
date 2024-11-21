def calculate(input_string):

    san_updown = 0
    san_leftright = 0
    
    rob_updown = 0
    rob_leftright = 0

    positions = []
    positions.append((san_updown, san_leftright))

    #loop for santa, from pos 1 in string, every 2nd character
    for i in range (0, len(input_string),2):
        char = input_string [i]
        if char == '^':
            san_updown += 1
        elif char == 'v':
            san_updown -= 1
        elif char == '>':
            san_leftright += 1
        elif char == '<':
            san_leftright -= 1
        if (san_updown, san_leftright) not in positions:
            positions.append((san_updown, san_leftright))

    #loop for robo, from pos 2 in string, every 2nd character
    for i in range (1, len(input_string),2):
        char = input_string [i]
        if char == '^':
            rob_updown += 1
        elif char == 'v':
            rob_updown -= 1
        elif char == '>':
            rob_leftright += 1
        elif char == '<':
            rob_leftright -= 1
        if (rob_updown, rob_leftright) not in positions:
            positions.append((rob_updown, rob_leftright))

    number_of_houses = len(positions)
    return f"Problem 3.2 Number of houses: {number_of_houses}"
