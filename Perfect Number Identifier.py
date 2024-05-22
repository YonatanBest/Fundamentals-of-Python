num = int(input("Enter a number: "))
sum = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("The number ", num, "is perfect number.")
else:
    print("The number ", num, "is not perfect number.")