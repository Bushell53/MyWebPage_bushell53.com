def calculate(input_string):
    lines = input_string.splitlines()  # Split the input into lines
    grid = [[0] * 1000 for _ in range(1000)]  # Initialize a 1000x1000 grid with all brightness levels at 0

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
                    grid[i][j] += 1  # Increase brightness by 1
                elif action == "off":
                    grid[i][j] = max(0, grid[i][j] - 1)  # Decrease brightness by 1, but not below 0
                elif action == "toggle":
                    grid[i][j] += 2  # Increase brightness by 2

    # Calculate the total brightness
    total_brightness = sum(sum(row) for row in grid)
    return f"Total brightness: {total_brightness}"
