print("MULTIPLICATION TABLE MAKER")
ask = eval(input("Enter a number to see its multiplication table: "))

print("MULTIPLICATION TABLE OF", ask)
for count in range(1, 11):
    asked = ask * count
    print(ask, "x", count, "=", asked)