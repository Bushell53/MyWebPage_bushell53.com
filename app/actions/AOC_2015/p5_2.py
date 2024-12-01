import re

def calculate(input_string):
    """
    Calculates the number of "nice" strings in the input.
    A "nice" string satisfies:
    1. Contains a pair of any two letters that appears at least twice without overlapping.
    2. Contains at least one letter that repeats with exactly one letter between them.
    """
    # Split the input into lines
    lines = input_string.splitlines()
    good_lines_count = 0  # Initialize count for "nice" lines

    # Iterate over each line
    for line in lines:
        # Debugging: Print the line being checked
        print(f"Checking line: {line}")

        # Check 1: Pair of letters appearing at least twice without overlapping
        pair_repetition = re.search(r'(\w{2}).*\1', line)
        if pair_repetition:
            print(f"  Pair repetition found: {pair_repetition.group(1)}")

        # Check 2: A letter that repeats with exactly one letter between
        repeat_with_one_between = re.search(r'(\w).\1', line)
        if repeat_with_one_between:
            print(f"  Repeated letter with one between found: {repeat_with_one_between.group(1)}")

        # Increment count if both checks pass
        if pair_repetition and repeat_with_one_between:
            print("  This line is nice!")
            good_lines_count += 1
        else:
            print("  This line is not nice.")

    # Return the count of good lines
    return f"Number of good lines: {good_lines_count}"

