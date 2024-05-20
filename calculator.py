# 1. We use def to define our functions (methods); after the def, we write the name of our function. We can make the function to receive a certain value we it is called by adding variable names in the bracket as of the example given in this program.
# 2. We use print() to display or print an information in the console.
# 3. We assign (set a value for) a variable by starting with the name of the variable, then the assignment operator(=), and finally the value we want to assign.
# 4. We use input() to accept a value from the user using the console. The input() always return the value in string, so we should convert it to a different data type as needed.
# 5. We use int(), Str(), float(), etc to convert from a certain data type to another one as needed.
# 6. We use if, elif, and else to excute a certain command if a certain, condition is met. Elif is set to check for a certain condition if one is not met. Else is used to do something if all the conditions are not met. Syntax: as of the example given in this program.
# 7. We use nameOfFunction() to call the function we have created.
# 8. We use return to return a certain value of the work (operation done) after the function is called and did something.
def calc(): #1
    print("Please choose one of the following operation \n 1. Addition \n 2. Substaction \n 3. Multiplication \n 4. Division") #2
    operation = int(input("Here: ")) #3, #4 and #5
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    if 1 == operation: #6
        print(sum_op(first_num, second_num))
    elif 2 == operation: #6
        print(sub_op(first_num, second_num))
    elif 3 == operation:
        print(mul_op(first_num, second_num))
    elif 4 == operation:
        print(div_op(first_num, second_num))
    else: #6
        print("please enter a correct operation")
        calc() #7
def sum_op(first_num, second_num):
    return first_num + second_num #8
def sub_op(first_num, second_num):
    return first_num - second_num
def mul_op(first_num, second_num):
    return first_num * second_num
def div_op(first_num, second_num):
    return first_num / second_num

calc()