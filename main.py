#coding assignment 3
#maximum age as 90

age = input("What is your current age? ")
#coverting input into integer
age_as_int = int(age)
remaining_age = 90 - age_as_int
days_remaining = remaining_age * 365
weeks_remaining = remaining_age * 52
months_remaining = remaining_age * 12
print(f"You have {days_remaining} Days, {weeks_remaining} weeks, {months_remaining} months left.")
