def add(P, Q):
    return P + Q
def substract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def division(P, Q):
    return P / Q
print("Please select the operation: ")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("d. Divide")
choice = input("Please enter your choice (a/b/c/d):")
num_1 = float(input("Enter the first number :  "))
num_2 = float(input("Enter the second number : "))
if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))
elif choice == 'b':
    print(num_1, " - ", num_2, " = ", substract(num_1, num_2))
elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", division(num_1, num_2))
else:
    print("This is an invalid input!")
