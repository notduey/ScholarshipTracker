#!/usr/bin/env python
"""
view scholarships
"""
import platform
import locale #for currency
from data import scholarships


if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "English_United States.1252")
else:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


def view_scholarship():
    """
    loop through scholarships
    """
    print("\nScholarships:\n")

    for i, row in enumerate(scholarships, start=1):
        #enumerate() function adds a counter to the list
        #start=1 starts the counter at 1 instead of 0
        print(f"{i}. {row[0]}") #prints scholarship number and name
        print(f" Link: {row[1]}")

        formatted = locale.currency(float(row[2]), grouping=True) #grouping=True adds commas
        print(f" Amount: {formatted}")

        print(f" Deadline: {row[3]}")
        print(f" Status: {row[4]}")
        print(f" Essay required: {row[5]}")

        if row[6]:
            print(f" Additional notes: {row[6]}\n")


def view_title():
    """
    loop through titles
    """
    print("\nScholarships:\n")
    for i, row in enumerate(scholarships, start=1):
        print(f"{i}. {row[0]}") #prints scholarship number and name
