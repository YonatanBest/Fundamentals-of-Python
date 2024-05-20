# 1. We use % (module) to find the reminder of a certain number when it is divided by a certain number.
# 2. We use ==, >=, <=, !=, > and < to check whether a certain value is equal to, greater than or equal etc. a certain value.
num = int(input("Enter the number you wanted to know whether even or odd: "))
if num % 2 == 0: #1 and #2
    print("The number", num, "is even.")
else:
    print("The number", num, "is odd.")