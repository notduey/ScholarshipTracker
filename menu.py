#!/usr/bin/env python
"""
menu file for scholarship tracker
"""
from add_edit_scholarship import add_scholarship
from manage_scholarship import manage_scholarship
from data import scholarships

def main_menu():
    """
    main menu that gives user to add, view/edit scholarships, or exit program"""

    while True:
        if scholarships:
            print("Main Menu\n")
            print("1. Add Scholarship\n"
                  "2. View/Edit Scholarships\n"
                  "3. Save and Exit Program\n")
        else:
            print("Main Menu\n")
            print("1. Add Scholarship\n"
                  "2. Save and Exit Program\n")

        choice = input("Enter your choice: ").strip()
        options = "1 or 2"
        options_range = ["1", "2"]

        if scholarships:
            options = "1, 2, or 3"
            options_range = ["1", "2", "3"]
        while choice not in options_range:
            choice = input(f"Invalid choice. Enter {options}: ").strip()

        if choice == "1":
            add_scholarship()
        elif choice == "2":
            if scholarships:
                manage_scholarship()
            else:
                print("\nSaving and exiting program...\n")
                break

        if scholarships:
            if choice == "3":
                print("\nSaving and exiting program...")
                break
