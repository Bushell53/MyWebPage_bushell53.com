import hashlib

def calculate(input_string):
    number = 0
    five_zero_pw = None

    while True:
        combined_input = f"{input_string}{number}"
        hash_object = hashlib.md5(combined_input.encode())
        md5_hash = hash_object.hexdigest()

        if five_zero_pw is None and md5_hash[:5] == "00000":
            five_zero_pw = f"For 4.1 the PW is {combined_input} and the hash was {md5_hash}"
            print(f"Found 5 zeros: {combined_input} -> {md5_hash}")

        if five_zero_pw is not None and md5_hash[:6] == "000000":
            six_zero_pw = f"for 4.2 the PW is {combined_input} and the hash was {md5_hash}"
            print(f"Found 6 zeros: {combined_input} -> {md5_hash}")

            return f"{five_zero_pw}<br>{six_zero_pw}"

        if number > 100_000_000:
            return "Tried 100 million hashes but didn't find both results."
        
        number += 1

