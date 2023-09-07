'''this program calculates compound interest.
The formula for calculatimg compound interest is A = p*(1 + r/n)**(n*t).
A is the amount gotten after the stated amount of time
p is the principal amount
r is the interest rate
n is the number of compounding period in a year
t is the amount of time in years the money is invested'''

#collecting user inputs
p = int(input('Please input your principal amount: $'))
t = int(input('Please input the amount of years your capital is invested: '))
r = int(input('Please input the interest rate: ')) / 100
n = 1

'''using the following values,
p = 50000
t = 4
r = 6/100
n = 1'''

#calculating the amount gained using the formula
A = p*(1 + r/n)**(n*t)

#printing the result 
print('The compound interest is $' + str(A))