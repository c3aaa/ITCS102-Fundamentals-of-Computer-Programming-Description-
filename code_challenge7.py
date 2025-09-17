import time

print("\nCOUNTDOWN TIMER SIMULATOR")
ask = eval(input("Enter the number starting for countdown: "))

for count in range(ask, 0, -1):
    for interval in range(1):
        print(count)
        time.sleep(1)
print("LIFT OFF!")