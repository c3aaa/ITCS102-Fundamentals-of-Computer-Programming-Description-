
name = input("Enter your name: ")
drama = ['Who Rules The World', 'The Long Ballad', 'Eternal Love of Dream', 'Ashes of Love', 'Love and Redemption']

drama.append("Love O2O")
print(f"\n---CHINESE DRAMA LIST COMPILATION, {name}---")
print(f"\nHello {name}, here is the updated list of Chinese Dramas: {drama}\n")
drama.insert(2, "Skate Into Love")
print(f"After inserting a new drama at index 2, the list is now: {drama}\n")
drama.remove("Ashes of Love")
print(f"After removing 'Ashes of Love', the list is now: {drama}\n")
drama.sort()
print(f"After sorting the list alphabetically, it is now: {drama}\n")
drama.reverse()
print(f"After reversing the list, it is now: {drama}\n")
drama.pop()
print(f"After popping the last drama from the list, it is now: {drama}\n")
print(f"Total number of dramas in the list: {len(drama)}\n")
print("------------------------------------------------------------------------------------------------------------------------------------------\n")

print("Thank You for Trying the Chinese Drama List Compilation!")
print("\t\t\t\t\t- by: Seeyah Zhou")
