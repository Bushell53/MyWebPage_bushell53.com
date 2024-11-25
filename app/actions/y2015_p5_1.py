def calculate(input_string):
    lines = input_string.splitlines()
    goodlines = []
    badlines = []

    for line in lines:
        lastchar = ""
        meetsfirstif = False
        vowelcount = 0

        # Check for forbidden substrings
        if any(sub in line for sub in ["ab", "cd", "pq", "xy"]):
            badlines.append(line)
            continue  # Skip further checks for this line

        # Check for repeated characters
        for char in line:
            if lastchar == char:  # If the current character is the same as the last one
                meetsfirstif = True
                break  # No need to check further; we found a repeated character
            lastchar = char  # Update the last character

        # If repeated characters are found, check for vowels
        if meetsfirstif:
            vowelcount = sum(1 for char in line if char in "aeiou")  # Count vowels
            if vowelcount >= 3:
                goodlines.append(line)
            else:
                badlines.append(line)
        else:
            badlines.append(line)

    # Count the number of good lines
    good_lines = len(goodlines)
    return f"Number of good lines: {good_lines}"
