from prettytable import PrettyTable

# Create a PrettyTable instance
table = PrettyTable()

# Step 2: Initialize counters
married_men_count = 0
single_men_count = 0
married_women_count = 0
single_women_count = 0

# Step 3: Initialize a list for eligible bachelors
eligible_bachelors = []

# Step 1: Read student records from a file (assuming a CSV format)
with open('student_records.csv', 'r') as file:
    lines = file.readlines()

# Step 4: Iterate through each student record
for line in lines:
    # Step 5: Split the record into its components (name, gender, age, marital status)
    parts = line.strip().split(',')
    
    
    name = parts[0]
    gender = parts[1]
    age = int(parts[2])
    marital_status = parts[3]

    # Define the table columns
    table.field_names = ["Name", "Gender", "Age", "Marital Status"]

    # Add data to the table
    table.add_row([name, gender,age,marital_status])

#Step 6: Update counters based on gender and marital status
    if gender == 'M':
        if marital_status == 'married':
            married_men_count += 1
        else:
            single_men_count += 1
            # Step 7: Check for eligible bachelors
            if age > 30:
                eligible_bachelors.append((name, age))
    else:
        if marital_status == 'married':
            married_women_count += 1
        else:
            single_women_count += 1




print("STUDENT SUMMARY REPORT FOR OUR SCHOOL")
# Print the table
print(table)

# Step 8: Print the student summary report
print(f"Married Men: {married_men_count}")
print(f"Single Men: {single_men_count}")
print(f"Married Women: {married_women_count}")
print(f"Single Women: {single_women_count}")

# Step 9: Print the eligible bachelor's report if there are eligible bachelors
if eligible_bachelors:
    print("\nEligible Bachelors:")
    for name, age in eligible_bachelors:
        print(f"{name}, Age: {age}")


