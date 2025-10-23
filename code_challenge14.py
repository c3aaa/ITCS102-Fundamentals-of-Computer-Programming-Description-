name = input("Enter your name: ")
print(f"---CHINESE DRAMA LIST MAKER, {name}---")

drama_list = []
while True:
    drama = input("Enter the Name of a Chinese Drama (type 'exit' to stop): ")
    if drama.lower() == 'exit':
        break
    drama_list.append(drama)
    print(f"'{drama}' has been added to the list. Continue.")
else:
    print("Error!")

print(f"\nChinese Drama List of {name.upper()}:")
for i in range(1, len(drama_list)+ 1):
    print(f" {i} - {drama_list[i - 1]}")
print("\nThank You for Trying the Chinese Drama List Maker!")




















