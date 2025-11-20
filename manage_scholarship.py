#!/usr/bin/env python
"""
manage scholarships
"""
from data import scholarships
from view_scholarship import view_scholarship, view_title

def manage_scholarship():
    """
    edit/delete scholarship
    """
    if not scholarships:
        print("No scholarships found.")
        return

    view_scholarship()
    choice = input("Enter D to delete, E to edit, or M to return to main menu: ").strip().upper()

    while choice not in ["D", "E", "M"]:
        print("Invalid choice. Enter D, E, or M.")
        choice = input(
            "Enter D to delete, E to edit, or M to return to main menu: "
            ).strip().upper()

    if choice == "D":
        delete_scholarship()
    elif choice == "E":
        print("Editing not yet implemented.")
    elif choice == "M":
        print("Returning to main menu.")
        return

def delete_scholarship():
    """
    delete scholarship
    """
    view_title()
    choice = input("Enter the scholarship number to delete (or press enter to cancel): ").strip()

    if not choice: #if choice is empty aka user pressed enter
        print("Delete cancelled.")
        return

    try:
        choice = int(choice)
    except ValueError as e:
        print("Invalid number. Error: ", e)
        return

    if choice < 1 or choice > len(scholarships):
        print("Number out of range.")
        return

    deleted = scholarships.pop(choice - 1) #choice - 1 because index starts at 0
    print(f"\"{deleted[0]}\" has been deleted.") #deleted[0] is 0th index of row
    #which is the name of the scholarship
