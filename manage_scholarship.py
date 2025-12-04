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
    choice = input("Enter E to edit, D to delete, or M to return to main menu: ").strip().upper()
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
    choice = input("Enter the scholarship number to delete (press enter to cancel): ").strip()

    if choice:
        while True:
            try:
                choice = int(choice)
                if choice <= 0 or choice > len(scholarships):
                    raise IndexError
                deleted = scholarships.pop(choice - 1) #choice - 1 because index starts at 0
                print(f"\"{deleted[0]}\" has been deleted.\n") # deleted[0] is the name index
                break
            except ValueError:
                choice = input("Invalid input. Enter a number: ").strip()
            except IndexError:
                choice = input(
                    f"Invalid number. Enter corresponding number 1-{len(scholarships)}: "
                    ).strip()
    else:
        print("Deletion cancelled.\n")

def edit_scholarship(): #MAKE NEW FILE TO STORE EDIT FUNCTIONS
    """
    edits scholarship info
    """
    view_title()
    choice = input("Enter the scholarship number to edit (press enter to cancel): ").strip()

    if choice:
        while True:
            try:
                choice = int(choice)
                if choice <= 0 or choice > len(scholarships):
                    raise IndexError
                scholarship = scholarships[choice - 1] #choice - 1 because index starts at 0
                break
            except ValueError:
                choice = input("Invalid input. Enter a number: ").strip()
            except IndexError:
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
        "\nEnter the corresponding number you want to edit (press enter to cancel): ").strip()
    print()
    if choice:
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            choice = input("Invalid choice. Enter a number 1-7: ")
    else:
        print("Edit cancelled.\n")
        return

    if choice == "1":
        name_input = input("Enter new name (press enter to cancel): ").strip()
        if name_input:
            scholarship[0] = name_input[0].upper() + name_input[1:]
            print(f"Name updated to: {scholarship[0]}\n")
        else:
            print("Edit cancelled.\n")
            return

    elif choice == "2":
        link_input = input(
            "Enter new link or press D to delete link (press enter to cancel): ").strip().lower()
        if link_input:
            if link_input == "d":
                scholarship[1] = "NO LINK"
                print("Link deleted.\n")
                return
            scholarship[1] = link_input
            print(f"Link updated to: {scholarship[1]}\n")
        else:
            print("Edit cancelled.\n")
            return

    elif choice == "3":
        amount_input = input("Enter new amount (press enter to cancel): ").strip()
        if amount_input:
            while True:
                try:
                    amount = float(amount_input.replace("$", "").replace(",", ""))
                    scholarship[2] = str(f"{amount:.2f}") #stores amount with 2 decimal places
                    formatted = locale.currency(amount, grouping=True) #format amount adding $ and ,
                    print(f"Amount updated to: {formatted}\n")
                    break
                except ValueError: #runs if amount couldn't be converted to float
                    amount_input = input("Invalid amount. Enter a number: ").strip()
        else:
            print("Edit cancelled.\n")
            return

    elif choice == "4":
        deadline_input = input("Enter new deadline MM/DD/YYYY (press enter to cancel): ").strip()
        if deadline_input:
            while True:
                try:
                    deadline_date = datetime.strptime(deadline_input, "%m/%d/%Y")
                    if platform.system() == "Windows":
                        scholarship[3] = deadline_date.strftime("%B %#d, %Y")
                    else:
                        scholarship[3] = deadline_date.strftime("%B %-d, %Y")
                    break
                except ValueError as e:
                    if "does not match format" in str(e):
                        deadline_input = input("Invalid date. Enter MM/DD/YYYY: ").strip()
                    elif "out of range" in str(e):
                        deadline_input = input("Date does not exist. Enter a valid date: ").strip()
                    else:
                        deadline_input = input(f"Unknown error: {e}.\nEnter a valid date:").strip()
            print(f"Deadline updated to: {scholarship[3]}\n")
        else:
            print("Edit cancelled.\n")
            return

    elif choice == "5":
        status_input = input(
            "\nEnter status incomplete/ongoing/complete (press enter to cancel): ").strip().upper()
        if status_input:
            while status_input not in ["INCOMPLETE", "ONGOING", "COMPLETE"]:
                status_input = input("Enter incomplete, ongoing, or complete: ").strip().upper()
            scholarship[4] = status_input
            print(f"Status updated to: {scholarship[4]}\n")
        else:
            print("Edit cancelled.\n")
            return

    elif choice == "6":
        essay_input = input(
            "Essay required? Press Y or N (press enter to cancel): ").strip().lower()
        if essay_input:
            while essay_input not in ["y", "n"]:
                essay_input = input("Invalid response. Enter Y or N: ").strip().lower()
            if essay_input == "y":
                scholarship[5] = "YES"
            elif essay_input == "n":
                scholarship[5] = "NO"
            print(f"Essay required updated to: {scholarship[5]}\n")
        else:
            print("Edit cancelled.\n")
            return

    elif choice == "7":
        note_input = input(
            "Press A to add to notes, R to replace/make notes, or D to delete notes "
            "(press enter to cancel): "
            ).strip().lower()
        if note_input:
            while note_input not in ["a", "r", "d"]:
                note_input = input("Invalid response. Enter E, R, or D: ").strip().lower()
            if note_input == "a":
                append = input("Enter text to add to notes (press enter to cancel): ").strip()
                if append:
                    scholarship[6] += " " + append
                    print(f"Notes updated to: {scholarship[6]}\n")
            elif note_input == "r":
                scholarship[6] = input("Enter new notes: ").strip()
                print("New notes added.\n")
            elif note_input == "d":
                scholarship[6] = ""
                print("Notes cleared.\n")
        else:
            print("Edit cancelled.\n")
            return
