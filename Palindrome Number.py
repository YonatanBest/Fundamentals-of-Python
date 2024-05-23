# 1. We use while as alternative of for loop. They have the same use, but one may be approprate for a certain situation.
# 2. We use statement_for_true condition statement_for_false to make the format more short and precise.

number = int(input("Enter a number: "))
num = number
num_new = 0

while num > 0: #1
    reminder = num % 10
    num = num // 10
    num_new = (num_new * 10) + reminder
print("The number is palindrome.") if number == num_new else print("The number is not palindrome.") #2