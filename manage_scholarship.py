#!/usr/bin/env python
"""
manage scholarships
"""
import locale
import platform
from datetime import datetime
from data import scholarships
from view_scholarship import view_scholarship, view_title

locale.setlocale(locale.LC_ALL, "en_US")

def manage_scholarship():
    """
    edit/delete scholarship
    """
    if not scholarships:
        print("No scholarships found.\n")
        return

    view_scholarship()
    choice = input(
        "Enter E to edit, D to delete, or M to return to main menu: "
    ).strip().upper()
    print()

    while choice not in ["D", "E", "M"]:
        choice = input(
            "Invalid choice. Enter D, E, or M: "
            ).strip().upper()

    if choice == "E":
        edit_scholarship()
    elif choice == "D":
        delete_scholarship()
    elif choice == "M":
        print("Returning to main menu.\n")
        return

def delete_scholarship():
    """
    delete scholarship
    """
    view_title()
    choice = input(
        "Enter the scholarship number to delete or press enter to cancel: "
    ).strip()

    if choice:
        while True:
            try:
                choice = int(choice)
                deleted = scholarships.pop(choice - 1) #choice - 1 because index starts at 0
                print(f"\"{deleted[0]}\" has been deleted.\n") #deleted[0] is 0th index of row
                #which is the name of the scholarship
                break
            except ValueError:
                choice = input("Invalid input. Enter a number: ")
            except IndexError:
                if len(scholarships) == 1:
                    choice = input(
                        "Invalid number. Enter corresponding number: "
                        ).strip()
                elif len(scholarships) > 1:
                    choice = input(
                        f"Invalid number. Enter corresponding number 1-{len(scholarships)}: "
                        ).strip()
    else:
        print("Deletion cancelled.\n")
        return

def edit_scholarship():
    """
    edits scholarship info
    """
    view_title()
    choice = input(
        "Enter the scholarship number to edit or press enter to cancel: "
        ).strip()

    if choice:
        while True:
            try:
                choice = int(choice)
                scholarship = scholarships[choice - 1] #choice - 1 because index starts at 0
                break
            except ValueError:
                choice = input("Invalid input. Enter a number: ").strip()
            except IndexError:
                if len(scholarships) == 1:
                    choice = input(
                        "Invalid number. Enter corresponding number: ").strip()
                elif len(scholarships) > 1:
                    choice = input(
                        f"Invalid number. Enter corresponding number 1-{len(scholarships)}: "
                        ).strip()
    else:
        print("Edit cancelled.\n")
        return

    print("\n1. Name")
    print("2. Link")
    print("3. Amount")
    print("4. Deadline")
    print("5. Status")
    print("6. Essay required")
    print("7. Notes")
    choice = input(
        "\nEnter the corresponding number you want to edit or press enter to cancel: "
        ).strip()
    print()
    if choice:
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            choice = input("Invalid choice. Enter a number 1-7: ")
    else:
        print("Edit cancelled.\n")
        return

    if choice == "1":
        name_input = input("Enter new name: ").strip()
        while not name_input:
            name_input = input("Name cannot be empty. Enter a name: ").strip()
        scholarship[0] = name_input[0].upper() + name_input[1:]
        print(f"Name updated to: {scholarship[0]}\n")

    elif choice == "2":
        link_input = input("Enter new link (Press enter to delete link): ").strip().lower()
        if link_input:
            scholarship[1] = link_input
        else:
            scholarship[1] = "NO LINK"
        print(f"Link updated to: {scholarship[1]}\n")

    elif choice == "3":
        amount_input = input("Enter new amount: ").strip() #asks user for new amount
        while True:
            try:
                amount = float(amount_input.replace("$", "").replace(",", ""))
                scholarship[2] = str(f"{amount:.2f}") #stores amount with 2 decimal places
                formatted = locale.currency(amount, grouping=True) #format amount adding $ and ,
                print(f"Amount updated to: {formatted}\n")
                break
            except ValueError: #runs if amount couldn't be converted to float
                amount_input = input("Invalid amount. Enter a number: ").strip()
                #asks user again then goes back to top of while loop

    elif choice == "4":
        deadline_input = input("Enter new deadline (MM/DD/YYYY): ").strip()
        while True:
            try:
                deadline_date = datetime.strptime(deadline_input, "%m/%d/%Y")
                if platform.system() == "Windows":
                    scholarship[3] = deadline_date.strftime("%B %#d, %Y")
                else:
                    scholarship[3] = deadline_date.strftime("%B %-d, %Y")
                break
            except ValueError:
                deadline_input = input("Invalid date format. Enter MM/DD/YYYY: ").strip()
        print(f"Deadline updated to: {scholarship[3]}\n")

    elif choice == "5":
        scholarship[4] = input(
            "\nEnter status (incomplete/ongoing/complete): "
        ).strip().upper()
        while scholarship[4] not in ["INCOMPLETE", "ONGOING", "COMPLETE"]:
            scholarship[4] = input("Enter incomplete, ongoing, or complete: ").strip().upper()
        print(f"Status updated to: {scholarship[4]}\n")

    elif choice == "6":
        essay_input = input("Essay required? (y/n): ").strip().lower()
        while essay_input not in ["y", "n"]:
            essay_input = input("Invalid response. Enter y or n: ").strip().lower()
        if essay_input == "y":
            scholarship[5] = "YES"
        elif essay_input == "n":
            scholarship[5] = "NO"
        print(f"Essay required updated to: {scholarship[5]}\n")

    elif choice == "7":
        scholarship[6] = input("Enter new notes: ").strip()
        print(f"New notes: {scholarship[6]}\n")
