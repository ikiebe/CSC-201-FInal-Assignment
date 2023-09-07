personal_status= input("Enter your status single or married:")
personal_allowance = 7000 if personal_status == "single" else 15000
income_tax=0
gross_income= int(input("enter your gross income"))
num_of_children = int(input("enter amount of children "))
child_allowances= 2000 * min(num_of_children, 12)
taxable_income= gross_income - (personal_allowance + child_allowances)
if taxable_income <= 1000:
    income_tax= 0
elif taxable_income <= 2000:
    income_tax = taxable_income * 0.1
elif taxable_income <= 4000:
    income_tax= taxable_income * 0.15
else:
    income_tax = taxable_income* 0.20
print("your income tax is :" ,income_tax)