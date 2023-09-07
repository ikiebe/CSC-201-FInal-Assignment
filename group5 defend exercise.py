#decalrong the variables
child_no = 0
tax_rate = 0
taxable_income = 0
net_income = 0
total_alw = 0
single_alw = 7000
married_alw = 15000
child_alw = 0

#collecting user inputs 
name = input("Please input your name: ")
gender = input("Please input your gender (M/F): ")
maritalStatus = input("Are you married? (Y/N): ")

#conditional statement to determine if the user has kids given that they're married
if maritalStatus == "Y":
    children = input("Do you have a child(ren)? (Y/N): ")
    if children == "Y":
        child_no = int(input("Please input the amount of child (in figure(s)): "))
        if child_no > 4:
            child_no = 4
    elif children == "N":
        child_no = 0
    child_alw = 2000*child_no
elif maritalStatus == "N":
     maritalStatus = "N"
gross_income = int(input("Please input your gross income: $"))
first_pay = input("Is this your first pay? (Y/N): ")

#function to calculate the taxable income of the user
def taxable_inc(gross_income, total_alw):
    taxable_income = gross_income - total_alw
    print("Your taxable income is $" + str(taxable_income))
    return taxable_income

#function to calculate the income tax and net income of the user
def inc_tax(taxable_income, first_pay):
    #conditional statement to determine the income tax and net income of the user given the condition that taxable income is less than or equal to $1000 and is the first payment
    if taxable_income <= 1000 and first_pay == "Y":
        tax_rate = 0
        income_tax = 0
        net_income = taxable_income - income_tax
        print("Your income tax is $" + str(income_tax))
        print("Your net income is $" + str(net_income))
    #conditional statement to determine the income tax and net income of the user given the condition that taxable income is less than or equal to $1000 and is not the first payment
    elif taxable_income <= 1000 and first_pay == "N":
        tax_rate = 0.1
        income_tax = tax_rate*taxable_income
        net_income = (taxable_income - income_tax) + total_alw
        print("Your income tax is $" + str(income_tax))
        print("Your net income is $" + str(net_income))
    #conditional statement to determine the income tax and net income of the user given the condition that taxable income is in the range of $1000 and $2000
    elif taxable_income > 1000 <= 2000:
        tax_rate = 0.15
        income_tax = tax_rate*taxable_income
        net_income = (taxable_income - income_tax) + total_alw
        print("Your income tax is $" + str(income_tax))
        print("Your net income is $" + str(net_income))
    #conditional statement to determine the income tax and net income of the user given the condition that taxable income is greater than $4000
    elif taxable_income > 4000:
        tax_rate = 20/100
        income_tax = taxable_income*tax_rate
        net_income = (taxable_income - income_tax) + total_alw
        print("Your income tax is $" + str(income_tax))

#conditional statement to determine the income tax and net income of the user given the user is male
if gender == "M":
    #conditional statement to determine the user's total allowance considering the conditions of marital status and whether they have a child(ren) or not (being yes or no)
    if maritalStatus == "Y" and children == 'Y':
        total_alw = married_alw + child_alw
        print("Your total allowance is $" + str(total_alw))
    elif maritalStatus == "Y" and children == "N":
        total_alw = married_alw
        print("Your total allowance is $" + str(total_alw))
    elif maritalStatus == "N":
        total_alw = single_alw
        print("Your total allowance is $" + str(total_alw))
    #to get the taxable income, we call and assign the function 'taxable_inc' to a variable
    taxable_income = taxable_inc(gross_income, total_alw)
    #we call the function 'inc_tax' to perform the operations that determines the income tax of the user
    inc_tax(taxable_income, first_pay)
    
#conditional statement to determine the income tax and net income of the user given the user is female
elif gender == "F":
    #due to the conditions in the given exercise, the allowance of a lady wether single or married is same as that of a single person
    total_alw = single_alw
    print("Your total allowance is $" + str(total_alw))
    #to get the taxable income, we call and assign the function 'taxable_inc' to a variable
    taxable_income = taxable_inc(gross_income, total_alw)
    #we call the function 'inc_tax' to perform the operations that determines the income tax of the user
    inc_tax(taxable_income, first_pay)
