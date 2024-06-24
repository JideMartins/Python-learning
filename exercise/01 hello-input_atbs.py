# This program says hello and asks for my name.

print("Hello")
print("What's your name?")  # asks for their name
my_name = input()
nameLength = len(my_name)
print("It's good to meet you, " + my_name)
print("The length of your name is: " + str(nameLength) + ".")

print("What is your age?")

# use the input function to assign value to your age when the user inputs age.
my_age = input()

# print the age + 5 years
print("In 5 years, you will be " + str(int(my_age) + 5) + " years old.")
