#this program takes the input of two numbers and calculates their sum, difference, product and quotient

#user introduction
print('Hi there, this program takes the input of two numbers and calculates their sum, difference, product and quotient')

#collecting user input
num_1 = int(input('Please input your first number: '))
num_2 = int(input('Please input your second number: '))

#calculating and printing the sum, difference, product and quotient of the two numbers the user input 
print('The sum of both number is ' + str(num_1 + num_2))
print('The difference of both number is ' + str(num_1 - num_2))
print('The product of both number is ' + str(num_1 * num_2))
print('The quotient of both number is ' + str(num_1 // num_2))