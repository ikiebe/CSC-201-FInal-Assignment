'''This program calculates the energy stored in a comndemser
The formula for energy stored in a condenser is (CV**2)/2 where C is the capacitance and V is the voltage(potential difference)'''

#collecting user values for C and V
c = float(input('Please input the value for your capacitance '))
v = float(input('Please input the value for your voltage (potential difference): '))

#calculating the energy stored using the stated formula 
step_1 = v**2
step_2 = c*step_1
step_3 = step_2/2

print(str(step_3) + "joules")