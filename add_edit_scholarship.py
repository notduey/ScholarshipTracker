#!/usr/bin/env python
"""
add scholarship
"""
import add_edit_functions as ae
from data import scholarships

def add_scholarship():

    """
    add scholarship with relevant information
    """

    name = ae.add_name()
    link = ae.add_link()
    amount = ae.add_amount()
    deadline = ae.add_deadline()
    status = ae.add_status()
    essay = ae.add_essay()
    notes = ae.add_notes()

    new_scholarship = [name, link, amount, deadline, status, essay, notes]
    scholarships.append(new_scholarship)

    print(f"\n{scholarships[-1][0]} was added!\n") #[-1] is last row, [0] is name index

def edit_choices(scholarship):
    """
    edit choices name, link, amount, deadline, status, essay required, notes"""
    print("\n1. Name"
          "\n2. Link"
          "\n3. Amount"
          "\n4. Deadline"
          "\n5. Status"
          "\n6. Essay required"
          "\n7. Notes")
    choice = input(
        "\nEnter the corresponding number you want to edit (press enter to cancel): ").strip()
    if choice:
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            choice = input("Invalid choice. Enter a number 1-7: ")
    else:
        print("Edit cancelled.\n")
        return
    if choice == "1":
        ae.edit_name(scholarship)
    elif choice == "2":
        ae.edit_link(scholarship)
    elif choice == "3":
        ae.edit_amount(scholarship)
    elif choice == "4":
        ae.edit_deadline(scholarship)
    elif choice == "5":
        ae.edit_status(scholarship)
    elif choice == "6":
        ae.edit_essay(scholarship)
    elif choice == "7":
        ae.edit_notes(scholarship)
