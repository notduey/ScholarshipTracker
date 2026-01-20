#!/usr/bin/env python
"""
add and edit choices
"""
import locale
import platform
from datetime import datetime

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "English_United States.1252")
else:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


def add_name():
    """
    add scholarship name and returns it
    """
    name_input = input("\nScholarship name (press enter to skip): ").strip()
    if name_input: #if name_input is not empty aka user didn't press enter without typing in name
        name = name_input[0].upper() + name_input[1:] #capitalizes first letter only
    else:
        name = "NO NAME"
    return name


def edit_name(scholarship):
    """
    edits scholarship name
    """
    name_input = input("\nEnter new name (press enter to cancel): ").strip()
    if name_input:
        scholarship[0] = name_input[0].upper() + name_input[1:]
        print(f"Name updated to: {scholarship[0]}\n")
    else:
        print("Edit cancelled.\n")


def add_link():
    """
    add scholarship link and returns it
    """
    link_input = input("Scholarship link (press enter to skip): ").strip()
    if link_input:
        link = link_input
    else:
        link = "NO LINK"
    return link


def edit_link(scholarship):
    """
    edits scholarship link
    """
    link_input = input(
        "\nEnter new link or press D to delete link (press enter to cancel): ").strip()
    if link_input:
        if link_input == "d":
            scholarship[1] = "NO LINK"
            print("Link deleted.\n")
            return
        scholarship[1] = link_input
        print(f"Link updated to: {scholarship[1]}\n")
    else:
        print("Edit cancelled.\n")


def add_amount():
    """
    add scholarship amount and returns it
    """
    amount_input = input("Scholarship amount (press enter defaults to $0): ").strip()
    while True:
        if amount_input:
            try:
                #tries removing $ and , that user might enter then converts string to float
                amount = float(amount_input.replace("$", "").replace(",", ""))
                break
            except ValueError:
                amount_input = input("Invalid amount. Enter a number:").strip()
        else:
            amount = float(0)
            break
    return amount


def edit_amount(scholarship):
    """
    edits scholarship amount"""
    amount_input = input("\nEnter new amount (press enter to cancel): ").strip()
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


def add_deadline():
    """
    add scholarship deadline and returns it
    """
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
    return deadline


def edit_deadline(scholarship):
    """
    edits scholarship deadline"""
    deadline_input = input("\nEnter new deadline MM/DD/YYYY (press enter to cancel): ").strip()
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


def add_status():
    """
    add scholarship status and returns it
    """
    status = input(
        "Scholarship status (incomplete/ongoing/complete): "
        ).strip().upper()
    while status not in ["INCOMPLETE", "ONGOING","COMPLETE"]:
        status = input("Enter incomplete, ongoing, or complete: ").strip().upper()
    return status


def edit_status(scholarship):
    """
    edits scholarship status incomplete/ongoing/complete"""
    status_input = input(
        "\nEnter status INCOMPLETE, ONGOING, or COMPLETE (press enter to cancel): ").strip().upper()
    if status_input:
        while status_input not in ["INCOMPLETE", "ONGOING", "COMPLETE"]:
            status_input = input("Enter INCOMPLETE, ONGOING, or COMPLETE: ").strip().upper()
        scholarship[4] = status_input
        print(f"Status updated to: {scholarship[4]}\n")
    else:
        print("Edit cancelled.\n")


def add_essay():
    """
    add scholarship essay requirement and returns it
    """
    essay_input = input("Essay required? Press Y or N: ").strip().lower()
    while essay_input not in ["y", "n"]:
        essay_input = input("Invalid response. Enter Y or N: ").strip().lower()
    if essay_input == "y":
        essay = "YES"
    else:
        essay = "NO"
    return essay


def edit_essay(scholarship):
    """
    edits scholarship essay requirement
    """
    essay_input = input("\nEssay required? Press Y or N (press enter to cancel): ").strip().lower()
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


def add_notes():
    """
    add scholarship notes and returns it
    """
    notes = input("Additional scholarship notes (press enter to skip): ").strip()
    return notes


def edit_notes(scholarship):
    """
    edits scholarship notes with option to add to, replace, or delete notes
    """
    note_input = input(
        "\nPress A to add to notes, R to replace/make notes, or D to delete notes "
        "(press enter to cancel): "
        ).strip().lower()
    if note_input:
        while note_input not in ["a", "r", "d"]:
            note_input = input("Invalid response. Enter A, R, or D: ").strip().lower()
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
