isdowty = True
sum = 0

while isdowty == True:
    conferm = input("Do you want to continue washing? (yez/nah): ")
    sum += 1
    if conferm.lower() == "yez":
        print("Wahh, you are so cleanie!")
        continue
    else:
        print("Washing ended.")
        break
print(f"You have washed {sum} times.") 