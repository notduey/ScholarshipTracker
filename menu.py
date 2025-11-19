#!/usr/bin/env python
"""
menu file for scholarship tracker
"""

def display_main_menu():
    """
    displays main menu
    """
    print("Main Menu")
    print("1. Add Scholarship")
    print("2. View/Edit Scholarships")
    print("3. Exit Program")

def main_menu():
    """
    main menu that gives user to add, view/edit scholarships, or exit program"""
    while True:
        display_main_menu()
        choice = input("Enter you choice:").strip()
        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Enter 1, 2, or, 3")
            continue #continue goes back to the start of the while loop

        if choice == "1":
            print("add scholarship (not implemented yet)")
        elif choice == "2":
            print("view/edit scholarships (not implemented yet)")
        elif choice == "3":
            print("exiting program")
            break #break ends the while loop
