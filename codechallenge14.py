import os
import json

os.system('cls')

print("STUDENT SYSTEM INFORMATION")
print("-------------------------------")

student_record = {}

while True:
    print("A - Add All Student Record")
    print("B - Print All Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - Exit System")

    choice = input("SELECT FROM THE OPTION ABOVE ---> ").upper()
    
    if choice == 'A':
        print("\nADDING STUDENT RECORD")
        id_no = input("Please input Student ID Number: ")

        first_name = input("Please input Student First Name: ").upper()
        second_name = input("Please input Student Second Name: ").upper()
        age = eval(input("Please input Student Age: "))
        course = input("Please input Student Course: ").upper()
        section = input("Please input Student Section: ").upper()
        email = input("Please input Student Email: ")

        student_record[id_no] = [first_name, second_name, age, course, section, email]
        print("DATA SAVED SUCCESSFULLY")
        os.system('cls')
        continue
    elif choice == 'B':
        print("PRINTING STUDENT RECORD")
        
        for i, j in student_record.items():
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
            continue

    elif choice == 'C':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Enter Student ID for Search: ")

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("--------------------------")
                print(f"\nRECORD FOUND for ID {search_id}!")
                for i in student_record[search_id]:
                    print(f"| {i}")
                print("--------------------------")
            else:
                print("NO RECORD INCLUDED!")
            break
        continue

    elif choice == 'D':
        os.system('cls')

        print("DELETE STUDENT RECORD")

        search_id = input("Enter Student ID for Search: ")

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("--------------------------")
                print(f"\nRECORD FOUND for ID {search_id}!")
                for i in student_record[search_id]:
                    print(f"| {i}")
                print("--------------------------")

                student_record.pop(search_id)
                print("\nSTUDENT RECORD DELETED!")
            else:
                print("NO RECORD INCLUDED!")
            break
        continue
    elif choice == 'E':

        search_id = input("Enter Student ID for Search: ")

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("--------------------------")
                print(f"\nRECORD FOUND for ID {search_id}!")
                for i in student_record[search_id]:
                    print(f"| {i}")
                print("--------------------------")

                first_name = input("Please input Student First Name: ").upper()
                second_name = input("Please input Student Second Name: ").upper()
                age = eval(input("Please input Student Age: "))
                course = input("Please input Student Course: ").upper()
                section = input("Please input Student Section: ").upper()
                email = input("Please input Student Email: ")

                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section
                student_record[search_id][5] = email

                print("DATA UPDATED!")
            else:
                print("NO RECORD INCLUDED!")
            break
        continue
    elif choice == 'F':
        print("EXPORT STUDENT DATA")

        with open('student_record.json', 'w') as new_file:
            json.dump(student_record, new_file, indent = 4)

        print("\nDATA EXPORTED TO JSON!")
        continue
    elif choice == 'G':
        print("EXIT SYSTEM")
        break
    else:
        print("SYSTEM DENIED. PLEASE TRY AGAIN!")


