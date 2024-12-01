def calculate(input_string):
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
        wrap = min(twoheight + twolength, twolength + twowidth, twowidth + twoheight)

        # Add to the total surface area
        total_surface_area += wrap + bow

    # Set the result to the total calculated surface area
    return f"Total Surface Area: {total_surface_area}"
