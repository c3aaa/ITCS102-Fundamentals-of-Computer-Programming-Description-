print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER!")

ask = str(input("What do you want your parrot to say? "))
repeat = eval(input("How many times do you want to repeat it? "))
print("Listen to your parrot:")
for count in range(repeat):
    print("🦜", "Squawk!", ask)