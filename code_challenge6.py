sum = 0

for zzz in range(7):
    ran_num = eval(input("Enter any number: "))
    if ran_num % 2:
        sum += ran_num
print("The sum of the odd numbers is:", sum)
