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
