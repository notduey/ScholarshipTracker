#!/usr/bin/env python
"""
manage scholarships
"""
from add_edit_scholarship import edit_choices
from data import scholarships
from view_scholarship import view_scholarship, view_title

def manage_scholarship():
    """
    view and manage scholarship menu
    """
    view_scholarship()
    choice = input("Enter E to edit, D to delete, or M to return to main menu: ").strip().upper()
    while choice not in ["E", "D", "M"]:
        choice = input("Invalid choice. Enter E, D, or M: ").strip().upper()
    if choice == "M":
        print("Returning to main menu.\n")
        return
    delete_edit_prompt(choice)

def delete_edit_prompt(choice):
    """
    delete or edit scholarship
    """
    view_title()
    prompt = "edit"
    if choice == "D":
        prompt = "delete"
    num_input = input(
        f"\nEnter the scholarship number to {prompt} (press enter to cancel): ").strip()

    if num_input:
        while True:
            try:
                num_input = int(num_input)
                if num_input <= 0 or num_input > len(scholarships):
                    raise IndexError
                if choice == "E":
                    scholarship = scholarships[num_input - 1] #choice - 1 because index starts at 0
                    edit_choices(scholarship)
                elif choice == "D":
                    name = scholarships[num_input - 1][0] #num_input - 1 is row index, 0 is name
                    confirm_input = input(
                        f"\nAre you sure you want to {name}? Press Y or N: ").strip().lower()
                    while confirm_input not in ["y","n"]:
                        confirm_input = input("Invalid response. Enter Y or N: ").strip().lower()
                    if confirm_input == "y":
                        deleted = scholarships.pop(num_input - 1)
                        print(f"\"{deleted[0]}\" has been deleted.\n") # deleted[0] is name index
                    else:
                        print("Delete cancelled.\n")
                        return
                break
            except ValueError:
                num_input = input("Invalid input. Enter a number: ").strip()
            except IndexError:
                num_input = input(
                    f"Invalid number. Enter corresponding number 1-{len(scholarships)}: "
                    ).strip()
    else:
        prompt = prompt.title()
        print(f"{prompt} cancelled. Returning to main menu.\n")
