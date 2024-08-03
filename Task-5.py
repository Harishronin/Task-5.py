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


def fibonacci(count):
	fib_list = [0, 1]

	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
										range(2, count)))

	return fib_list[:count]

print(fibonacci(10))
