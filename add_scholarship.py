#!/usr/bin/env python
"""
add scholarship
"""
import platform
from datetime import datetime
from data import scholarships

def add_scholarship():
    """
    add scholarship with relevant information
    """
    name_input = input("Scholarship name (press enter to skip): ").strip()
    if name_input: #if name_input is not empty aka user didn't press enter without typing in name
        name = name_input[0].upper() + name_input[1:] #capitalizes first letter only,
        #unlike title(), if the user capitalizes any following letters, they will stay capitalized
    else:
        name = "NO NAME"

    link_input = input("Scholarship link (press enter to skip): ").strip().lower()
    if link_input:
        link = link_input
    else:
        link = "NO LINK"

    amount_input = input("Scholarship amount (press enter defaults to $0): ").strip()
    while True:
        if amount_input:
            try:
                #triess removing $ and , that user might enter then converts string to float
                amount = float(amount_input.replace("$", "").replace(",", ""))
                break
            except ValueError:
                amount_input = input("Invalid amount. Enter a number:").strip()
        else:
            amount = float(0)
            break


    deadline_input = input("Scholarship deadline MM/DD/YYYY (press enter to skip): ").strip()
    while True:
        if deadline_input:
            try:
                deadline_date = datetime.strptime(deadline_input, "%m/%d/%Y")
                if platform.system() == "Windows":
                    deadline = deadline_date.strftime("%B %#d, %Y") #formats date for windows
                else:
                    deadline = deadline_date.strftime("%B %-d, %Y") #formats date for macos/linx
                break
            except ValueError as e:
                if "does not match format" in str(e):
                    deadline_input = input("Invalid date. Enter MM/DD/YYYY: ").strip()
                elif "out of range" in str(e):
                    deadline_input = input("Date does not exist. Enter a valid date: ").strip()
                else:
                    deadline_input = input(f"Unknown error: {e}.\nEnter a valid date:")
        else:
            deadline = "DEADLINE N/A"
            break

    status = input(
        "Scholarship status (incomplete/ongoing/complete): "
        ).strip().upper()
    while status not in ["INCOMPLETE", "ONGOING","COMPLETE"]:
        status = input("Enter incomplete, ongoing, or complete: ").strip().upper()

    essay_input = input("Essay required? Press Y or N: ").strip().lower()
    while essay_input not in ["Y", "N"]:
        essay_input = input("Invalid response. Enter Y or N: ").strip().lower()
    if essay_input == "y":
        essay = "YES"
    else:
        essay = "NO"

    notes = input("Additional scholarship notes (press enter to skip): ").strip()
    print()

    new_scholarship = [name, link, amount, deadline, status, essay, notes]
    scholarships.append(new_scholarship)

    print("Scholarship added!\n")
