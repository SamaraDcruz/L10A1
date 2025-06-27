medical = input("Do you have a medical reason? (Y/N)")


if medical == "Y":
    print("You are allowed to take the exam.")
else:

    attendance = int(input("Enter your attendance perncentage :  "))


if attendance > 75:
    print("You are allowed to take the exam.")
else:
    print("You are NOT allowed to take the exam.")