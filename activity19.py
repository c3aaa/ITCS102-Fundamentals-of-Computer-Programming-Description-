for i in range(1, 11, 1):
    for x in range(1, i, 1):
        print("", end=" ")
    for y in range(1, i, -1):
        print("*", end=" ")
    for c in range(i, 10, 1):
        print("*", end=" ")
    print("")
