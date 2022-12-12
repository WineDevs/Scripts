# Lambda is an inline function

# For example let's create simple lambda

lam = lambda a,b : a # It return "a" variable

print(lam(10,20))# Print 10

# But now let's try to make a lambda that will count numbers

count = lambda a,b : a+b # It return a+b variables

print(count(10,20)) # Print 30

lenght = lambda array : len(array)

print(lenght([1,2,3,4,5]))# Return 5 (lenght of array)

'''
plus = lambda a,b : a+b
minus = lambda a,b : a-b
multiply = lambda a,b : a*b
divide = lambda a,b: a/b

print(plus(2,2))#Integer
print(minus(10,5))#Integer
print(multiply(2,2))#Integer
print(divide(10,2))#Float
'''