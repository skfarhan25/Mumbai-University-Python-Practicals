import datetime

Today = datetime.date.today()
Temp = Today
print(f"Today: {Today}")
for i in range(1, 11):
    Temp += datetime.timedelta(days=14)
    print(f"Week {i}: {Temp}")