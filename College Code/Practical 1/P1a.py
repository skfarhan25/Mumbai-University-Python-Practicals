from datetime import date

Current_Date = date.today()

UserName = input("Enter Your Name: ")
UserAge = int(input("Enter Your Age: "))
Year  = (Current_Date.year - UserAge) + 100
print(f"{UserName}, You will turn 100 in the year {Year}")