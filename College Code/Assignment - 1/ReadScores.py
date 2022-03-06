UserScore = int(input("Enter score: "))

if UserScore >= 95:
    print("Your Grade is A+.")
elif UserScore >= 85:
    print("Your Grade is A.")
elif UserScore >= 70:
    print("Your Grade is C.")
elif UserScore >= 40:
    print("Your Grade is D.")
elif UserScore < 40:
    print("You Failed.")