def calculate(input_string):
    # Perform the bracket difference calculation
    open_count = 0
    close_count = 0
    for char in input_string:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if close_count > open_count:
            return f"Sum at imbalance: {open_count + close_count}"
    else:
        return f"Difference: {open_count - close_count} (Open - Close)"
