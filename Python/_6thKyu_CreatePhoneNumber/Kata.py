# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.


def create_phone_number(n):
    result_string = ""
    if len(n) == 10:
        for digit in range(len(n)):
            if digit == 0:
                result_string += f"({str(n[digit])}"
            elif digit == 2:
                result_string += f"{str(n[digit])}) "
            elif digit == 5:
                result_string += f"{str(n[digit])}-"
            else:
                result_string += str(n[digit])
        return result_string
    else:
        return "You entered the incorrect number of digits for a phone number"
