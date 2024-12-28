"""
Name:Harish kumar
Program1:excepted output for following python code
data=[10, 501, 37, 22, 109, 999, 87, 351]
result = filter (lambda x : x>4,data)
print (list(result))
date:02-Aug-2024
"""

data=[10, 501, 37, 22, 109, 999, 87, 351]
result = filter (lambda x : x>4,data)
print (list(result))


"""
Name:Harish kumar
Program2:write a python code using lambda function to check every element of a list is integer or string[10, 501, 37, 22, 109, 999, 87, 351]
date:02-Aug-2024
"""
data = [10, 501, 37, 22, 109, 999, 87, 351]
result = all(map(lambda x: isinstance(x, int), data))
print("All elements are integers:", result)

"""
Name:Harish kumar
Program3:using python lambda function create a fibonacci series from 1 to 50 elements
date:02-Aug-2024
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
