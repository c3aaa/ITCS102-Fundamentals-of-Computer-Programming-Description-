print("THE FACTORIAL PROGRAM")

number = eval(input("Enter any number: "))
factorial = 1
for zzz in range(number, 0, -1):
  factorial *= zzz
print("The factorial of", number, "is", factorial)
