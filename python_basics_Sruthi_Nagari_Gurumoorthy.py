# Task 1
name="Alpha"
age = 87
height = 6.1
is_student = True
print (name, age, height, is_student)


# Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format: Name: <name> | Age: <age> | Height: <height> | Student: <is_student>
print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")

# Task 3: Arithmetic Operations Using the age variable, calculate and print:Age in months, Age in days (assume 365 days/year), The remainder when age is divided by 7, Age raised to the power of 2
age_in_months = age * 12
age_in_days = age * 365
age_remainder = age % 7
age_power_of_2 = age ** 2
print ("age_in_months is:", age*12 ,  "\n age_in_days is:", age * 365, "\n age_remainder is:", age % 7, "\n age_power_of_2 is:", age ** 2)

