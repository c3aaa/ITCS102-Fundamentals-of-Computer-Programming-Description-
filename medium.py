# number = eval(input("Enter the column number for multiplication table: "))

# for i in range(1, 11, 1):
#     for j in range(1, number + 1, 1):
#         print(f"{i} x {j} = {i * j}", end="\t")
#     print()

for i in range(1, 7, 1):
    for x in range(7, i, -1):
        print(" ", end=" ")
    for j in range(1, i, 1):
        print(" * ", end=" ")
    print()