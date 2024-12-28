"""
Name:Harish kumar
Program1:excepted output for following python code
data=[10, 501, 37, 22, 109, 999, 87, 351]
result = filter (lambda x : x>4,data)
print (list(result))
date:28-dec-2024
"""

data=[10, 501, 37, 22, 109, 999, 87, 351]
result = filter (lambda x : x>4,data)
print (list(result))


"""
Name:Harish kumar
Program2:write a python code using lambda function to check every element of a list is integer or string[10, 501, 37, 22, 109, 999, 87, 351]
date:28-dec-2024
"""
data = [10, 501, 37, 22, 109, 999, 87, 351]
result = all(map(lambda x: isinstance(x, int), data))
print("All elements are integers:", result)

"""
Name:Harish kumar
Program3:using python lambda function create a fibonacci series from 1 to 50 elements
date:28-dec-2024
"""

from functools import reduce

# Generate the Fibonacci series using lambda and reduce
fib_series = reduce(
    lambda acc, _: acc + [acc[-1] + acc[-2]],
    range(50 - 2),  # 50 elements total, we already have 2 seed values
    [0, 1]          # Initial seed values for Fibonacci
)

# Output the series
print(fib_series)

"""
Name:Harish kumar
Program4: write a python function to validate the regular expression for the following:
a.Email address
b.Mobile numbers of bangladesh
c.Telephone numbers of USA
d.16 character alpha-numneric password composed of alphabets of uppercase,lowercase,special character,numbers
date:28-dec-2024
"""

import re


def validate_input(input_value, validation_type):
    patterns = {
        "email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "mobile_bd": r"^(?:\+8801|01)[3-9]\d{8}$",  # Bangladesh mobile numbers
        "phone_usa": r"^\+1-\d{3}-\d{3}-\d{4}$",  # USA phone numbers
        "password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"
        # 16-character alphanumeric password
    }

    # regex 
    pattern = patterns.get(validation_type)
    if not pattern:
        raise ValueError("Invalid validation type specified.")

    # Validate input against the pattern
    return bool(re.match(pattern, input_value))


# Example 
if __name__ == "__main__":
    # Email validation
    print(validate_input("example@mail.com", "email"))  # True
    print(validate_input("wrongemail.com", "email"))  # False

    # Bangladesh mobile number validation
    print(validate_input("+8801756781234", "mobile_bd"))  # True
    print(validate_input("+8800156781234", "mobile_bd"))  # False

    # USA telephone number validation
    print(validate_input("+1-555-123-4567", "phone_usa"))  # True
    print(validate_input("555-123-4567", "phone_usa"))  # False

    # Password validation
    print(validate_input("Abcdef@123456789", "password"))  # True
    print(validate_input("Abcdef1234567890", "password"))  # False
