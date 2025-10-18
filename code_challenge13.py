name = input("Enter your name: ")
print("ODD NUMBER SUMMATION PROGRAM, press 0 to stop.\n")

con = True
sum = 0
odd = " "
while con == True:
    num = eval(input(f"Enter a random number, {name}: "))
    if num == 0:
        con = False
        print("Program ended.")
        break
    elif num % 2 == 1:
        sum += num
        odd += str(num) + " "
        continue
    else:
        print("Invalid input!")
        continue

print(f"\nHello {name}, the sum of odd numbers is: {sum}")
print(f"List of odd numbers:{odd}")