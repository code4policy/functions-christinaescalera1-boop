def add (a, b):
	return a + b

def multiply (a, b):
	return a * b

def subtract (a, b):
	return a - b 

def divide (a, b):
	if b == 0:
		raise ZeroDivisionError ("Can not Divide by zero")
	return a / b 

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

def square(a):
	return a ** 2

def cube (a):
	return a ** 3

def square_n_times (number, n)
	return number ** n 