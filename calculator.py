def calc():
    print("Please choose one of the following operation \n 1. Addition \n 2. Substaction \n 3. Multiplication \n 4. Division")
    operation = int(input("Here: "))
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    if 1 == operation:
        print(sum_op(first_num, second_num))
    elif 2 == operation:
        print(sub_op(first_num, second_num))
    elif 3 == operation:
        print(mul_op(first_num, second_num))
    elif 4 == operation:
        print(div_op(first_num, second_num))
    else:
        print("please enter a correct operation")
        calc()
def sum_op(first_num, second_num):
    return first_num + second_num
def sub_op(first_num, second_num):
    return first_num - second_num
def mul_op(first_num, second_num):
    return first_num * second_num
def div_op(first_num, second_num):
    return first_num / second_num

calc()