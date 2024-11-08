# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("what is your student name?")
print(name)
# student_name = input('What is your student name')
# print("Hi " + student_name)

# TODO: Ask the user for their age and store it in a variable
age= input("how old are you?")
print(age) 

# TODO: Print a greeting using the name and age variables
print("Hi my name is " + name + "I am " + age )
#---------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input( "enter the length of the rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("enter the width of the rectangle: "))
# TODO: Calculate the area of the rectangle
area = length * width 
# TODO: Print the result
print("the area of the rectangle is", area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
celsius = float(input("enter the temperature in celsius: "))

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit = (celsius * 9/5 ) + 32
# TODO: Print the result rounded to two decimal places
print("the fahrenheit is", fahrenheit)



