units = 24
def days_hours(no_days):
    if no_days>0:
       return f"{no_days} days are {no_days*24} hours"
    elif no_days == 0:
       return "you entered 0 please enter a positive number"
    else:
        print("You eneterd a negative one!")

usr=input("How many days u want in hours?\n")
if usr.isdigit():
    print(days_hours(int(usr)))
else:
    print("Enter a valid number")