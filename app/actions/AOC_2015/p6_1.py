def calculate(input_string):
    lines = input_string.splitlines()  # Split the input into lines
    grid = [[False] * 1000 for _ in range(1000)]  # Initialize a 1000x1000 grid with all lights off (False)

    for line in lines:
        # Parse the command and coordinates from the input
        parts = line.split()
        if parts[0] == "turn":
            action = parts[1]  # "on" or "off"
            start_coords = list(map(int, parts[2].split(',')))  # Extract start coordinates
            end_coords = list(map(int, parts[4].split(',')))  # Extract end coordinates
        elif parts[0] == "toggle":
            action = "toggle"
            start_coords = list(map(int, parts[1].split(',')))
            end_coords = list(map(int, parts[3].split(',')))

        # Apply the command to the grid
        for i in range(start_coords[0], end_coords[0] + 1):  # Iterate through rows
            for j in range(start_coords[1], end_coords[1] + 1):  # Iterate through columns
                if action == "on":
                    grid[i][j] = True  # Turn on the light
                elif action == "off":
                    grid[i][j] = False  # Turn off the light
                elif action == "toggle":
                    grid[i][j] = not grid[i][j]  # Toggle the light state

    # Count the number of lights that are on
    lights_on = sum(row.count(True) for row in grid)
    return f"Number of lights that are on: {lights_on}"
