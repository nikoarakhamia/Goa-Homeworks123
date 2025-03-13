age = int(input("Enter your age: "))

Experience = int(input("Enter your experience: "))


if age >= 18 and Experience >= 1:
    print("You can take driver license")
elif age >= 18 and Experience < 1:
    print("Sorry you can not take driver license, you are not experienced enough")
elif age < 18 and Experience > 1:
    print("Sorry you can not take driver license, you are not aged enough")
else: 
    print("You can not take driver license")
    