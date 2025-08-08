name = input("Ni hao, what's your name?")
print("Welcome to Zhou Yiran's Fantasy Realm,", name)

import time
time.sleep(2) 

response = input(f"Ni hao ma, {name}?") 

if response.lower () in ("good", "alright", "fine", "okay"):

    print("That's good!")
    
else:
        print("I hope you're still well")