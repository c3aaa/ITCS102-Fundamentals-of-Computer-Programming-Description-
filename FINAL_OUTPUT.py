import time
import os
import random

time.sleep(1)
print("\t\t\t\033[35mINTERACTIVE MENU PROGRAM\033[0m")
time.sleep(1)
print("\t\t\t\033[35mPython Programming - Final Output\033[0m")
time.sleep(1)
print("\t\t\t\033[35mBy: Seeyah Zhou\033[0m")
time.sleep(1)
os.system('cls')

time.sleep(1)
print("Levia: On the first breath of the ocean breeze,")
time.sleep(2)
print("\t\ta new journey begins...")
time.sleep(4)
os.system('cls')
enter = input("Dear traveler, let your finger press '1' and see how magic began... \n")
os.system('cls')

if enter == '1':
    print("Entering the realm...")
    time.sleep(1)
    os.system('cls')
else:
    print("Invalid input. Exiting program.")
    exit()

print("Levia: As the sacred water flowing in the ocean solidifies,")
time.sleep(2)
print("\t\tthe ancient gate is formed...")
time.sleep(3)
os.system('cls')
name = input("To enter a name must be whispered with courage --> ")
os.system('cls')

time.sleep(2)
print(f"Levia: Welcome, {name}! You have entered the world of" \
      "\n\t\t\t'NIVIVERSE'") #nivi means show sa latin
time.sleep(2)

while True:
    con = input("\nLevia: Shall we sail into the deepest mysteries of the ocean? (yes/no): ").lower()
    os.system('cls')

    if con == 'yes':
        time.sleep(3)
        print("\nProceeding into the endless depths...")
        time.sleep(3)
        os.system('cls')
        break

    elif con == 'no':
        print("\nLevia: From the echoes under the ocean, I thank you.")
        exit()
        
    else: 
        print("Invalid. Choose 'yes' or 'no'")
        time.sleep(3)
        os.system('cls')


print("\nUnfolding...")
time.sleep(2)
os.system('cls')

inter_menu = {}

while True:
    print("\t\t-----------------------------------------")
    print("\t\t\t\t\033[31mMAIN PORTAL\033[0m")
    print("\n\t\t\tA - Realm of Identity")
    print("\t\t\tB - Realm of Purpose")
    print("\t\t\tC - Realm of Knowledge")
    print("\t\t\tD - Realm of Resources")
    print("\t\t\tE - Exit Niviverse")
    print("\t\t-----------------------------------------")

    time.sleep(2)
    choice = input("\nLevia: Your destiny awaits." \
                   "\nLevia: Choose your path and let your soul guide you: ").upper()
    os.system('cls')

    if choice == 'A':
        print("Diving to the Realm of Identity...")
        time.sleep(3)
        os.system('cls')
        while True:
            print("\t\t---------------------------------")
            print("\t\t\t\033[31mREALM OF IDENTITY\033[0m")
            print("\n\t\t1 - Levia's Story")
            print("\t\t2 - Niviverse Origin")
            print("\t\t3 - Exit Realm of Identity")
            print("\t\t---------------------------------")


            real_iden = input(f"\nLevia: Every soul has a story." \
                              f"\nEnter the path where you think your heart belongs, {name}: ")
            
            if real_iden == '1':
                time.sleep(2)
                os.system('cls')
                print("Discovering Levia's Story...")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                print("\t\t\033[31mLevia's Story\033[0m")
                time.sleep(2)
                print("\nLevia, known among the tides as Leviathan.")
                time.sleep(2)
                print("The Guardian of the endless ocean.")
                time.sleep(2)
                print("Born from the whispers of the ancient civilian,")
                time.sleep(2)
                print("Who swims where the sun shines and the moon lights.")
                time.sleep(2)
                print("She guides the travelers who dare to flow into the depths.")
                time.sleep(2)
                print("\nIn the deep, dark, and lonely sea,")
                time.sleep(2)
                print("She shows the path hidden from those who do not seek.")
                time.sleep(2)
                print("For those who listen to the ocean's song,")
                time.sleep(2)
                print("Levia reveals the secrets... of the Niviverse.")
                time.sleep(2)

                while True:
                    quit = input("\n\nTouch '1' to return: ")
                    os.system('cls')

                    if quit == '1':
                        print("Returning...")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Invalid pathway. Try again.")
                        time.sleep(2)
                        os.system('cls')

            elif real_iden == '2':
                os.system('cls')
                print("Discovering Niviverse Origin...")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                print("\t\t\033[31mNiniverse Origin\033[0m")
                time.sleep(2)
                print("\nIn the beginning, there was only the vast ocean,")
                time.sleep(2)
                print("Beneath the waves of magical seas,")
                time.sleep(2)
                print("Each current drifts with hidden mystery.")
                time.sleep(2)
                print("Dive in, let your curiosity drown in the sea")
                time.sleep(2)
                print("And discover what they call NIVIVERSE. ")
                time.sleep(2)
                print("A realm where knowledge flows like waves—")
                time.sleep(2)
                print("Where every fish seeks in every caves.")
                time.sleep(2)
                print("A world where learning is an endless tide,")
                time.sleep(2)
                print("And every soul finds its guide.")
                time.sleep(2)

                while True:
                    quit = input("\n\nTouch '1' to return: ")
                    os.system('cls')

                    if quit == '1':
                        print("Returning...")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Invalid pathway. Try again.")
                        time.sleep(2)
                        os.system('cls')

            elif real_iden == '3':
                time.sleep(1)
                os.system('cls')
                print("Exiting Realm of Identity...")
                time.sleep(2)
                os.system('cls')
                print("\nReturning to Main Portal...")
                break

            else:
                print("Invalid pathway. Try again.")
                time.sleep(2)
                os.system('cls')

    elif choice == 'B':
        print("Diving to the Realm of Purpose...")
        time.sleep(3)
        os.system('cls')
        while True:
            print("\t\t---------------------------------")
            print("\t\t\t\033[31mREALM OF PURPOSE\033[0m")
            print("\n\t\t1 - Program Details") #include the about the program, purpose, and objective
            print("\t\t2 - How to Use the System") #step-by-step process on how to use it
            print("\t\t3 - Exit Realm of Purpose")
            print("\t\t---------------------------------")


            real_pur = input(f"\nLevia: Every door has its destiny." \
                             f"\nEnter the path where you think your soul belongs, {name}: ")
            
            if real_pur == '1':
                os.system('cls')
                print("Entering Program Details...")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                time.sleep(2)
                
                print("\t\t\033[31mABOUT THE PROGRAM\033[0m")
                print("\n\t\tThis program known as")
                print("\t\tNiviverse was created to")
                print("\t\tassist the users to learn")
                print("\t\tbasic python programming and " \
                "\n\t\taccess resources effectively.")
                time.sleep(2)
                print("\n\t\tIt guides the user through")
                print("\t\tlearning about the python") 
                print("\t\t(programming language) and")
                print("\t\tadditionally material for")
                print("\t\tinteractive approach and")
                print("\t\tuser-friendly environment.")

                time.sleep(3)
                print("\n\n\t\t\033[31mPURPOSE\033[0m")
                print("\t\t - Accommodate self-paced learners")
                print("\t\t - Provide easy access and user-" \
                      "\n\t\tfriendly educational resources ")
                print("\t\t - Enhance knowledge ")
                print("\t\t - Encourage continuous learning")
                time.sleep(3)

                while True:
                    quit = input("\nTouch '1' to return: ")
                    os.system('cls')

                    if quit == '1':
                        print("Returning...")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Invalid pathway. Try again.")
                        time.sleep(2)
                        os.system('cls')

            elif real_pur == '2':
                os.system('cls')
                print("Entering How to Use the System...")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                time.sleep(2)
                print("033[31mHOW TO USE THE SYSTEM\033[0m")
                print("\n1. Upon entering the Niviverse,")
                print("   you will be greeted by Levia,")
                print("   the Guardian of the Ocean.")
                time.sleep(2)
                print("\n2. Choose your desired realm")
                print("   from the Main Portal to explore")
                print("   different aspects of Python programming.")
                time.sleep(2)
                print("\n3. Follow the prompts and instructions")
                print("   provided by Levia to navigate")
                print("   through each realm.")
                time.sleep(2)
                print("\n4. Engage with the content,")
                print("   complete activities, and absorb")
                print("   the knowledge presented.")
                time.sleep(2)
                print("\n5. When you wish to exit a realm,")
                print("   select the option to return")
                print("   to the Main Portal.")
                time.sleep(2)
                print("\n6. To exit the Niviverse,")
                print("   choose the exit option")
                print("   from the Main Portal.")
                time.sleep(2)

                while True:
                    quit = input("\n\nTouch '1' to return: ")
                    os.system('cls')

                    if quit == '1':
                        print("Returning...")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Invalid pathway. Try again.")
                        time.sleep(2)
                        os.system('cls')

            elif real_pur == '3':
                time.sleep(1)
                os.system('cls')
                print("Exiting Realm of Purpose...")
                time.sleep(2)
                os.system('cls')
                break

            else:
                print("Invalid pathway. Try again.")
                time.sleep(2)
                os.system('cls')

    elif choice == 'C':
        print("Diving to the Realm of Knowledge...")
        time.sleep(3)
        os.system('cls')
        while True:
            print("\t\t----------------------------------")
            print("\t\t\t\033[31mREALM OF KNOWLEDGE\033[0m")
            print("\n\t\t1 - Printing Statements")
            print(" \t\t2 - Variable and Data Types")
            print(" \t\t3 - Operator Statements")
            print(" \t\t4 - Conditional Statements")
            print(" \t\t5 - Loops")
            print(" \t\t6 - Lists")
            print(" \t\t7 - Function")
            print(" \t\t8 - Exit to the Main Portal")
            print("\t\t----------------------------------")

            topic_choice = input("\nLevia: Select a topic to explore: ")
            topic_choice == True
            os.system('cls')
            
            if topic_choice == '1':
                print("\nKnowlwedge selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Printing Statements.")
                time.sleep(2)
                os.system('cls')

                print("\n\t\t\t\t\033[31mPRINTING STATEMENTS\033[0m")
                print("   \n\t\t\tIn Python, printing statements is done " \
                "          \n\t\t\tusing the 'print()' function. It is also" \
                "          \n\t\t\tutilized to display messsages, numbers," \
                "          \n\t\t\tand results on the screen; one of the" \
                "          \n\t\t\tbasic functions in Python programming.")

                while True:
                    example = input("\n\nLevia: Would you like to reveal some examples of printing statements? (yes/no): ").lower()
                    os.system('cls')
                    if example == 'yes':
                        os.system('cls')
                        time.sleep(2)
                        print("\nLevia: Here are some examples of printing statements in Python:\n")
                        print("1. Printing a simple message:")
                        print('   print("Hello, World!")')
                        print("   Output: Hello, World!\n")
                        time.sleep(2)
                        print("2. Printing numbers:")
                        print("   print(3)")
                        print("   Output: 3\n")
                        time.sleep(2)
                        print("3. Printing multiple items:")
                        print('   print("The answer is", 3)')
                        print("   Output: The answer is 3\n")
                        time.sleep(2)
                        print("4. Formatted printing:")
                        print('   name = "Yiran"\n   age = 25\n   print(f"{name} is {age} years old.")')
                        print("   Output: Yiran is 25 years old.\n")
                        time.sleep(2)
                        print("5. Printing with special characters:")
                        print('   print("Hello\\nWorld!")')
                        print("   Output:\n   Hello\n   World!\n")
                        time.sleep(2)

                        print("\n\nLevia: These are just a few examples of how to use the print() function in Python." \
                        " \nFeel free to experiment with different messages and formats to see how it works!")
                        time.sleep(2)

                        while True:
                            done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                            os.system('cls')
                            if done == '1':
                                print("Returning...")
                                time.sleep(2)
                                os.system('cls')
                                break
                            else:
                                print("Invalid. Try again.")
                                time.sleep(2)
                                os.system('cls')

                            
                    elif example == 'no':
                        print("Levia: Alright! See you next time.")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Levia: Invalid input.")
                        time.sleep(2)
                        os.system('cls')

            
            elif topic_choice == '2':
                print("\nKnowlwedge selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Variables and Data Types.")
                time.sleep(2)
                os.system('cls')

                print("\n\t\t\t\t\t\033[31mVARIABLES AND DATA TYPES\033[0m")
                print("        \n\t\t\tIn Python, variables are used to store data values. " \
                "              \n\t\t\tA variable is created when you assign a value to it. " \
                "              \n\t\t\tIt acts like a container for storing data. Python " \
                "              \n\t\t\tallows the user to store text, numbers, and more" \
                "              \n\t\t\tcomplex data types using variables." \
                "              \n\n\t\t\tData types refer to the classification of data " \
                "              \n\t\t\tthat tells the compiler or interpreter how the " \
                "              \n\t\t\tprogram intends to use the data. Python has several " \
                "              \n\t\t\tbuilt-in data types.")

                while True:
                    example = input("\n\nLevia: Would you like to explore variables and data types? (yes/no): ").lower()
                    os.system('cls')

                    if example == 'yes':
                        print("\t\t----------------------------------------")
                        print("\t\t\t\033[31mVariables and Data Types\033[0m")
                        print(" \n\t\t1 - Example of Variables")
                        print(" \t\t2 - Purpose and Examples of Data Types")
                        print(" \t\t3 - Exit to the Variable and Data Types")
                        print("\t\t----------------------------------------")


                        choice = input("\nLevia: Select a pathway: ")
                        if choice == '1':
                            os.system('cls')
                            time.sleep(2)
                            print("\033[31mVariables Example:\033[0m")
                            print("\n\033[35mText (String) Variable:\033[0m")
                            print('   name = "Yiran"')
                            print("Output: The variable 'name' now holds the string value 'Yiran'.\n")
                            time.sleep(2)

                            print("\n\033[35mInteger Variable:\033[0m")
                            print('   age = 25')
                            print("Output: The variable 'age' now holds the integer value 25.\n")
                            time.sleep(2)

                            print("\n\033[35mFloat Variable:\033[0m")
                            print('   height = 5.9')
                            print("Output: The variable 'height' now holds the float value 5.9.\n")
                            time.sleep(2)

                            print("\n\033[35mBoolean Variable:\033[0m")
                            print('   yiranismyhusband = True')
                            time.sleep(2)

                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '2':
                            os.system('cls')
                            time.sleep(2)
                            print("\033[31mData Types Purpose:\033[0m")
                            print("\n\n1. String (str): Used to store text data.")
                            print("Example: 'Hello, World!'\n")
                            time.sleep(2)
                            print("\n2. Integer (int): Used to store whole numbers.")
                            print("Example: 42\n")
                            time.sleep(2)
                            print("\n3. Float (float): Used to store decimal numbers.")
                            print("Example: 3.14\n")
                            time.sleep(2)
                            print("\n4. Boolean (bool): Used to store True or False values.")
                            print("Example: True\n")
                            time.sleep(2)
                            print("\n5. List: Used to store multiple items in a single variable.")
                            print("Example: [1, 2, 3]\n")
                            time.sleep(2)
                            print("\n6. Dictionary (dict): Used to store key-value pairs.")
                            print("Example: {'name': 'Yiran', 'age': 25}\n")

                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '3':
                            print("Returning...")
                            time.sleep(2)
                            os.system('cls')
                            break
                    elif example == 'no':
                        print("Levia: Alright! See you next time.")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Levia: Invalid choice.")
                        time.sleep(2)
                        os.system('cls')
                    
            elif topic_choice == '3':
                print("\nKnowledge Selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Operators Statements.")
                time.sleep(2)
                os.system('cls')

                print("\n\t\t\t\t\033[31mOPERATORS STATEMENTS\033[0m")
                print("        \n\t\t\tIn Python, operators are special symbols " \
                "              \n\t\t\tthat perform operations on variables and values. " \
                "              \n\t\t\tThey are used to manipulate data and perform " \
                "              \n\t\t\tcalculations. Operators can be classified into " \
                "              \n\t\t\tseveral types based on the operations they perform.")

                while True:
                    example = input("\n\nLevia: Would you like to explore Operators Statements? (yes/no): ").lower()
                    os.system('cls')

                    if example == 'yes':
                        os.system('cls')
                        time.sleep(2)
                        
                        print("\t\t---------------------------------------------------")
                        print("\t\t\t\033[31mMAJOR TYPES OF OPERATORS IN PYTHON\033[0m")
                        print(" \n\t\t1 - Arithmetic Operators")
                        print(" \t\t2 - Comparison Operators")
                        print(" \t\t3 - Assignment Operators")
                        print(" \t\t4 - Logical Operators")
                        print(" \t\t5 - Exit Operators Section")
                        print("\t\t---------------------------------------------------")


                        choice = input("\nLevia: Select a pathway: ")
                        if choice == '1':
                            os.system('cls')
                            time.sleep(2)
                            print("\nArithmetic Operators: Used to perform mathematical")
                            print("operations like addition, subtraction, multiplication,"
                                " and division.\n")
                            
                            print("\033[35mOPERATORS:\033[0m")
                            print("  +  : Addition")
                            print("example: 5 + 3 = 8\n")

                            print("  -  : Subtraction")
                            print("example: 5 - 3 = 2\n")

                            print("  *  : Multiplication")
                            print("example: 5 * 3 = 15\n")

                            print("  /  : Division")
                            print("example: 15 / 3 = 5\n")

                            print("  %  : Modulus")
                            print("example: 5 % 3 = 2\n")

                            print("  ** : Exponentiation")
                            print("example: 2 ** 3 = 8\n")

                            while True:
                                done = input("\n\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '2':
                            os.system('cls')
                            time.sleep(2)
                            print("\nComparison Operators: Used to compare two values")
                            print("and return a boolean result (True or False).\n")
                            print("\033[35mOPERATORS:\033[0m")
                            print("  == : Equal to")
                            print("example: 5 == 3 -> False\n")

                            print("  != : Not equal to")
                            print("example: 5 != 3 -> True\n")

                            print("  >  : Greater than")
                            print("example: 5 > 3 -> True\n")

                            print("  <  : Less than")
                            print("example: 5 < 3 -> False\n")

                            print("  >= : Greater than or equal to")
                            print("example: 5 >= 3 -> True\n")

                            print("  <= : Less than or equal to")
                            print("example: 5 <= 3 -> False\n")

                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '3':
                            os.system('cls')
                            time.sleep(2)
                            print("\nAssignment Operators: Used to assign values to variables.\n")
                            print("\033[35mOPERATORS:\033[0m")
                            print("  =  : Simple assignment")
                            print("example: x = 5 assigns the value 5 to variable x\n")

                            print("  += : Add and assign")
                            print("example: x += 3 is equivalent to x = x + 3\n")

                            print("  -= : Subtract and assign")
                            print("example: x -= 3 is equivalent to x = x - 3\n")

                            print("  *= : Multiply and assign")
                            print("example: x *= 3 is equivalent to x = x * 3\n")

                            print("  /= : Divide and assign")
                            print("example: x /= 3 is equivalent to x = x / 3\n")
                            done = input("\nDid you learn it all? If yes, press '1' to return: ")
                            os.system('cls')
                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')


                        elif choice == '4':
                            os.system('cls')
                            time.sleep(2)
                            print("\nLogical Operators: Used to combine conditional statements.\n")
                            print("\033[35mOPERATORS:\033[0m")
                            print("  and : Returns True if both statements are true")
                            print("example: (5 > 3) and (2 < 4) -> True\n")

                            print("  or  : Returns True if one of the statements is true")
                            print("example: (5 > 3) or (2 > 4) -> True\n")

                            print("  not : Reverses the result, returns False if the result is true")
                            print("example: not(5 > 3) -> False\n")
                            
                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '5':
                            print("Exiting Operators Section...")
                            time.sleep(2)
                            os.system('cls')
                            break
                        else:
                            print("Levia: Wrong destination!")
                            time.sleep(2)
                            os.system('cls')

                    elif example == 'no':
                        print("Levia: Alright! See you next time.")
                        time.sleep(2)
                        os.system('cls')

                        break
                    else:
                        print("Levia: Wrong pathway.")
                        time.sleep(2)
                        os.system('cls')


            elif topic_choice == '4':
                print("\nKnowledge Selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Conditional Operators.")
                time.sleep(2)
                os.system('cls')

                print("\n\t\t\t\t\033[31mCONDITIONAL STATEMENTS\033[0m")
                print("        \n\t\t\tIn Python, conditional statements also" \
                "              \n\t\t\tclassifed as Ternary Operators and are" \
                "              \n\t\t\tused to perform different actions based" \
                "              \n\t\t\ton whether acertain condition is true or " \
                "              \n\t\t\tfalse. They allowed the program to make " \
                "              \n\t\t\tdecisions and execute different blocks" \
                "              \n\t\t\tof code accordingly (if-else statements).")


                print("\n\n\033[35mIt answers the question: If a condition is true, then what should be chosen?" \
                    " \nOtherwise, what value should be chosen?\033[0m")

                print("\n\033[35mCondition: This is a boolean expression that evaluates to either True or False." \
                    " \nIf the condition is True, the first value is returned; otherwise, the second value is returned.\033[0m")

                while True:
                    example = input("\nLevia: Would you like to explore Operators Statements? (yes/no): ").lower()
                    os.system('cls')
                    if example == 'yes':
                        os.system('cls')
                        time.sleep(2)
                        print("\nLevia: Here are some examples of Conditional Operators in Python:")
                        print("\n1. Basic Conditional Operator:")
                        print('   result = "Yes" if True else "No"')
                        print("   Output: Yes\n")
                        time.sleep(2)
                        print("\n2. Conditional Operator with Variables:")
                        print('   age = 20\n   status = "Adult" if age >=18 else "Minor"')
                        print("   Output: Adult\n")
                        time.sleep(2)
                        print("\n3. Nested Conditional Operator:")
                        print('   score = 85\n   grade = "A" if score >= 90 else "B" if score >= 80 else "C"')
                        print("   Output: B\n")
                        time.sleep(2)
                        print("These examples demonstrate how conditional operators can be used to make decisions in Python code.")
                        
                        while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                    elif example == 'no':
                        print("Levia: Alright! See you next time. ")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Levia: Wrong pathway.")
                        time.sleep(2)
                        os.system('cls')

            elif topic_choice == '5':
                print("\nKnowledge Selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Loops.")
                time.sleep(2)
                os.system('cls')

                print("\n\t\t\t\t\033[31mLOOPS\033[0m")
                print("        \n\t\tIn Python, loops are used to execute a block of code " \
                "             \n\t\trepeatedly for a certain number of times or " \
                "              \n\t\twhile a specific condition is met. Loops help " \
                "             \n\t\tto automate repetitive tasks and make the code more efficient.")

                while True:
                    example = input("\n\nLevia: Would you like to explore Operators Statements? (yes/no): ").lower()
                    os.system('cls')
                    if example == 'yes':
                        os.system('cls')
                        time.sleep(2)
                        print("\t\t----------------------------------------")
                        print("\t\t\t\033[31mTYPES OF LOOPS IN PYTHON\033[0m")
                        print(" \n\t\t1 - For Loop")
                        print(" \t\t2 - While Loop")
                        print(" \t\t3 - Exit to the Main Menu")
                        print("\t\t----------------------------------------")

                        choice = input("\nLevia: Select a pathway: ")
                        if choice == '1':
                            os.system('cls')
                            time.sleep(2)
                            print("\nFOR LOOP: Used to iterate over a sequence (like a list, tuple, or string);" \
                            " \nthe loop will execute a block of code for each item in the sequence.\n")

                            print("\n\033[35mHow it Works:\033[0m")
                            print("1. The loop starts by defining a variable that takes the value of each item in the sequence.")
                            print("2. The block of code inside the loop is executed for each item in the sequence.")
                            print("3. The loop continues until all items in the sequence have been processed.\n")

                            print("\n\033[35mExample of For Loop:\033[0m")
                            print("example = ['yiran', 'my', 'husband']\n")
                            print("for example in example:")
                            print("    print(example)")
                            time.sleep(2)
                            print("\nOutput:")
                            print("yiran")
                            print("my")
                            print("husband\n")

                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '2':
                            os.system('cls')
                            time.sleep(2)
                            print("\nWHILE LOOP: Used to execute a block of code as long as a specified condition is true.\n")

                            print("\n\033[35mHow it Works:\033[0m")
                            print("1. The loop starts by checking the condition.")
                            print("2. If the condition is true, the block of code inside the loop is executed.")
                            print("3. After executing the block, the condition is checked again.")
                            print("4. The loop continues until the condition becomes false.\n")

                            print("\n\033[35mexample of While Loop:\033[0m")
                            print("count = 0\n")
                            print("while count < 5:")
                            print("    print(count)")
                            print("    count += 1")
                            time.sleep(2)
                            print("\nOutput:")
                            print("0")
                            print("1")
                            print("2")
                            print("3")
                            print("4\n")

                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')
                        
                        elif choice == '3':
                            print("Exiting Loops Section...")
                            time.sleep(2)
                            os.system('cls')
                            break
                        else:
                            print("Levia: Wrong destination!")
                            time.sleep(2)
                            os.system('cls')

                    elif example == 'no':
                        print("Levia: Alright! See you next time.")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Levia: Wrong pathway.")
                        time.sleep(2)
                        os.system('cls')

            elif topic_choice == '6':
                print("\nKnowledge Selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Lists.")
                time.sleep(2)
                os.system('cls')

                print("\n\t\t\t\t\t\t\033[31mLISTS\033[0m")
                print("        \n\t\t\tIn Python, a list is a built-in data type that " \
                "              \n\t\t\tallows you to store multiple data in a single " \
                "              \n\t\t\tvariable. Lists are ordered, changeable, and " \
                "              \n\t\t\tallow duplicate values. They are one of the " \
                "              \n\t\t\tmost commonly used data structures in Python." \
                "              \n\t\t\tLists can hold items of different data types, " \
                "              \n\t\t\tsuch as strings, integers, floats, and even other " \
                "              \n\t\t\tlists.")

                while True:
                    example = input("\n\nLevia: Would you like to explore Operators Statements? (yes/no): ").lower()
                    os.system('cls')
                    if example == 'yes':
                        os.system('cls')
                        time.sleep(2)

                        print("\t\t----------------------------------")
                        print("\t\t\t\033[31mLIST OPERATIONS\033[0m")
                        print("\n\t\t 1 - How it Works")
                        print("\n\t\t 2 - List Methods and Examples")
                        print("\n\t\t 3 - Exit List Section")
                        print("\t\t----------------------------------")

                        choice = input("\nLevia: Select a pathway: ")
                        if choice == '1':
                            os.system('cls')
                            time.sleep(2)
                            print("\033[35mHow Lists Works:\033[0m")
                            print("When creating a list, Python store the item in order" \
                                "\nbased on their position. Each item in the list has an index" \
                                "\nstarting from 0 for the first item, 1 for the second item," \
                                "\nand so on. You can access, modify, and manipulate the items" \
                                "\nin the list using their index positions.\n")
                                
                            print("\n\033[35mExample of Creating Lists:\033[0m")
                            print("example = ['yiran', 'my', 'husband']\n")
                            print("Accessing List Items:\n")
                            print("print(example[0])  # Output: yiran")
                            time.sleep(2)
                            print("print(example[1])  # Output: my")
                            time.sleep(2)
                            print("print(example[2])  # Output: husband\n")

                            while True:
                                done = input("\n\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '2':
                            print("\033[35mList Methods and Examples:\033[0m")
                            os.system('cls')
                            time.sleep(2)
                            print("1. append(): Adds an item to the end of the list.")
                            print("example = ['yiran', 'my']\n")
                            print("example.append('husband')\n")
                            print("Output: ['yiran', 'my', 'husband']\n")
                            time.sleep(2)

                            print("2. remove(): Removes the first occurrence of a specified item.")
                            print("example = ['yiran', 'my', 'husband']\n")
                            print("example.remove('my')\n")
                            print("Output: ['yiran', 'husband']\n")
                            time.sleep(2)

                            print("3. pop(): Removes and returns an item at a specified index.")
                            print("example = ['yiran', 'my', 'husband']\n")
                            print("item = example.pop(1)\n")
                            print("Output: item = 'my', example = ['yiran', 'husband']\n")
                            time.sleep(2)

                            print("4. sort(): Sorts the items in the list in ascending order.")
                            print("example = [3, 1, 2]\n")
                            print("example.sort()\n")
                            print("Output: [1, 2, 3]\n")
                            time.sleep(2)

                            print("5. reverse(): Reverses the order of items in the list.")
                            print("example = ['yiran', 'my', 'husband']\n")
                            print("example.reverse()\n")
                            print("Output: ['husband', 'my', 'yiran']\n")
                            time.sleep(2)

                            print("\033[35mThese are just a few examples of list methods in Python."
                                "\nFeel free to explore more methods and functionalities to"
                                "\nmanipulate lists according to your needs!\033[0m")

                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '3':
                            print("Exiting Lists Section...")
                            time.sleep(2)
                            os.system('cls')
                            break
                        else:
                            print("Levia: Wrong destination!")
                            time.sleep(2)
                            os.system('cls')

                    elif example == 'no':
                        print("Levia: Alright! See you next time.")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Levia: Wrong pathway.")
                        time.sleep(2)
                        os.system('cls')

            elif topic_choice == '7':
                print("\nKnowledge Selected")
                time.sleep(2)
                os.system('cls')
                print("Unfolding...")
                time.sleep(1)
                os.system('cls')
                print(f"Levia: Greetings, {name}! Welcome to the world of Functions.")
                time.sleep(2)
                os.system('cls')


                print("\n\t\t\t\t\t\t\033[31mFUNCTIONS\033[0m")
                print("        \n\t\t\tIn Python, a function is a block of reusable " \
                "              \n\t\t\tcode that performs a specific task. Functions " \
                "              \n\t\t\thelp to organize code, improve readability, and " \
                "              \n\t\t\tallow for code reuse. They can take inputs, " \
                "              \n\t\t\tprocess data, and return outputs.")

                while True:
                    example = input("\n\nLevia: Would you like to explore Operators Statements? (yes/no): ").lower()
                    os.system('cls')
                    if example == 'yes':
                        os.system('cls')
                        time.sleep(2)
                        print("\t\t-----------------------------------")
                        print("\t\t\t\033[31mFUNCTIONS IN PYTHON\033[0m")
                        print("\n\t\t 1 - How it Works")
                        print("\t\t 2 - Function Examples")
                        print("\t\t 3 - Exit Functions Section")
                        print("\t\t-----------------------------------")

                        choice = input("\n\nLevia: Select a pathway: ")
                        if choice == '1':
                            os.system('cls')
                            time.sleep(2)
                            print("\033[35mHow Function Works:\033[0m")
                            print("1. Defining a Function: You define a function using the 'def' keyword,")
                            print("   followed by the function name and parentheses ().\n")
                            print("2. Function Parameters: You can specify parameters inside the parentheses")
                            print("   to accept inputs when the function is called.\n")
                            print("3. Function Body: The block of code inside the function is indented and")
                            print("   contains the instructions to be executed when the function is called.\n")
                            print("4. Calling a Function: You call a function by using its name followed by")
                            print("   parentheses (). You can pass arguments to the function if it has parameters.\n")
                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')


                        elif choice == '2':
                            print("\033[35mFunctions Examples:\033[0m")
                            os.system('cls')
                            time.sleep(2)
                            print("1. Simple Function without Parameters:")
                            print("def greet():")
                            print("    print('Hello, World!')\n")
                            print("greet()  # Output: Hello, World!\n")
                            time.sleep(2)

                            print("2. Function with Parameters:")
                            print("def add(a, b):")
                            print("    return a + b\n")
                            print("result = add(3, 5)")
                            print("print(result)  # Output: 8\n")
                            time.sleep(2)

                            print("3. Function with Default Parameter:")
                            print("def greet(name='Guest'):")
                            print("    print(f'Hello, {name}!')\n")
                            print("greet()          # Output: Hello, Guest!")
                            print("greet('Yiran')  # Output: Hello, Yiran!\n")
                            time.sleep(2)

                            print("\033[35mThese examples demonstrate how to define and use functions in Python."
                                "\nFeel free to create your own functions to perform various tasks!\033[0m")
                            
                            while True:
                                done = input("\nLevia: Did you learn it all? If yes, press '1' to return: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                        elif choice == '3':
                            print("Exiting Functions Section...")
                            time.sleep(2)
                            os.system('cls')
                            break
                        else:
                            print("Levia: Wrong destination!")
                            time.sleep(2)
                            os.system('cls')

                    elif example == 'no':
                        print("Levia: Alright! See you next time.")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Levia: Wrong pathway.")
                        time.sleep(2)
                        os.system('cls')

            elif topic_choice == '8':
                print("\nReturning to Main Portal...")
                time.sleep(1)
                os.system('cls')
                break
            else:
                print("\nLevia: Invalid selection. Please choose a valid topic.")
                time.sleep(2)
                os.system('cls')

    elif choice == 'D':
        print("Diving to the Realm of Additional Resources...")
        time.sleep(3)
        os.system('cls')

        while True:
            print("\t\t-----------------------------------")
            print("\t\t\t\033[31mREALM OF RESOURCES\033[0m")
            print("\n\t\t1 - Challenges" \
            "\n\t\t2 - Study Tips" \
            "\n\t\t3 - Motivational Quotes" \
            "\n\t\t4 - Exit to the Main Portal")
            print("\t\t-----------------------------------")

            resource_choice = input("\nSelect a pathway: ")

            if resource_choice == '1':
                os.system('cls')
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                print("Get ready to challenge.")
                time.sleep(2)
                os.system('cls')

                while True:
                    print("\t\t\t\033[31mGUESSING GAME\033[0m")
                    print("\n\t\t 1 - About the Game")
                    print("\t\t 2 - Play")
                    print("\t\t 3 - Exit Challenge")

                    choice = input("\nPick your pathway: ")

                    if choice == '1':
                        os.system('cls')
                        print("\t\t\t\033[31mABOUT THE GAME\033[0m")
                        print("Setup: One player picks a number within a range (1 - 100)")
                        print("Gameplay: The guesser will enter a number until he/she gets" \
                              "\nthe final answer.")
                        print("Win: Few guesses wins!")

                        while True:
                            exit = input("\nExit Game. Press '1': ")
                            if exit == '1':
                                os.system('cls')
                                print("Exiting game...")
                                time.sleep(2)
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print("Invalid pathway. Try again.")
                                time.sleep(2)
                                os.system('cls')

                    elif choice == '2':
                        os.system('cls')
                        time.sleep(2)
                        print("Unfolding...")
                        time.sleep(2)
                        os.system('cls')

                        print("\t\t\t\033[31mGUESSING GAME\033[0m")

                        random_value = random.randint(1,100)
                        tries = 0
                        con = True

                        while con == True:
                            user = input("Guess a random number from 1 - 100 " \
                            "(Press 'x' to quit): ")

                            if user.lower() == 'x':
                                os.system('cls')
                                print("Exiting game...")
                                time.sleep(2)
                                os.system('cls')
                                break
                            
                            num = int(user)
                            tries += 1
                            if num == random_value:
                                print("Congrats! You won.")
                                print(f"The random value is {random_value}.")
                                print("You guessed {tries} times.")
                                break
                            else:
                                print("Opps, try again!")
                                continue

                    elif choice == '3':
                        os.system('cls')
                        time.sleep(2)
                        print("Exiting game...")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        print("Invalid pathway.")
                        time.sleep(2)
                        os.system('cls')

            elif resource_choice == '2':
                os.system('cls')
                time.sleep(2)
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                print("\t\t\033[35mSTUDY TIPS\033[0m")
                print("\n- Practice everyday")
                print("- Learn by doing, not by reading")
                print("- Breakdown problems into small pieces")
                print("- Practice with simple projects")
                print("- Learn to code and understand the errors")
                print("- Take advatange of online practice sites")

                while True:
                    exit = input("\n\nQuit. Press '1': ")

                    if exit == '1':
                        os.system('cls')
                        print("Exiting...")
                        time.sleep(2)
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print("Invalid. Try again.")
                        time.sleep(2)
                        os.system('cls')
    
            elif resource_choice == '3':
                os.system('cls')
                time.sleep(2)
                print("Unfolding...")
                time.sleep(2)
                os.system('cls')
                while True:
                    print("\t\t-----------------------------------------")
                    print("\t\t\t\033[31mOpen when you're feeling\033[0m")
                    print("\n\t\t 1 - down")
                    print("\t\t 2 - sad")
                    print("\t\t 3 - unmotivated")
                    print("\t\t 4 - stuck")
                    print("\t\t 5 - stress")
                    print("\t\t 6 - tired")
                    print("\t\t 7 - exit")
                    print("\t\t-----------------------------------------")

                    feeling = input("\nLevia: What are you feeling as of the moment? ")

                    if feeling == '1':
                        os.system('cls')
                        print("You'll never find a rainbow if" \
                              "\nyou're looking down." \
                              "\n— Charlie Chaplin")
                        while True:
                                done = input("\nLevia: Feeling good? Press '1' to exit: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                    elif feeling == '2':
                        os.system('cls')
                        print("Even the worst days have an ending,"\
                              "\nand the best day have a beginning." \
                              "\n— Jennifer Coletta")
                        while True:
                                done = input("\nLevia: Feeling good? Press '1' to exit: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')
                    
                    elif feeling == '3':
                        os.system('cls')
                        print("Nobody's perfect so give yourself credit" \
                              "\nfor everything you're doing right, and be" \
                              "\nkind to yourself when you struggle." \
                              "\n- Lori Deschene")
                        while True:
                                done = input("\nLevia: Feeling good? Press '1' to exit: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                    elif feeling == '4':
                        os.system('cls')
                        print("You don't have to see the whole staircase," \
                              "\njust take the first step." \
                              "\n— Lori Deschene")
                        
                        while True:
                                done = input("\nLevia: Feeling good? Press '1' to exit: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                    elif feeling == '5':
                        os.system('cls')
                        print("In the middle of difficulty lies opportunity." \
                              "\n— Albert Einstein")
                        
                        while True:
                                done = input("\nLevia: Feeling good? Press '1' to exit: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')

                    elif feeling == '6':
                        os.system('cls')
                        print("If you get tired, learn to rest, not to quit." \
                              "\n— Banksy")
                        
                        while True:
                                done = input("\nLevia: Feeling good? Press '1' to exit: ")
                                os.system('cls')
                                if done == '1':
                                    print("Returning...")
                                    time.sleep(2)
                                    os.system('cls')
                                    break
                                else:
                                    print("Levia: Invalid. Try again.")
                                    time.sleep(2)
                                    os.system('cls')
                    
                    elif feeling == '7':
                        os.system('cls')
                        print("Exiting...")
                        time.sleep(2)
                        os.system('cls')
                        break

                    else:
                        print("\nInvalid pathway. Try again.")
                        time.sleep(2)
                        os.system('cls')

                                    
            elif resource_choice == '4':
                print("\nReturning to Main Menu...")
                time.sleep(1)
                os.system('cls')
                break

    elif choice == 'E':
        print("\nExiting the Niviverse. Thank you for using the Niviverse as Interactive Menu Program!")
        time.sleep(3)
        os.system('cls')
        exit()

    else:
        print("\nInvalid portal. Please choose A, B, C, D, or E.")
        time.sleep(2)
        os.system('cls')


