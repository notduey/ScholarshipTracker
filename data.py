#!/usr/bin/env python
"""
data file for scholarship tracker
"""
import csv


SCHOLARSHIPS_FILE = "scholarships.csv"

scholarships = []

def load_scholarships():
    """
    loads scholarships from scholarships.csv
    """
    scholarships.clear()
    #clears list just in case this function is called multiple times,
    #it'll keep appending to the same list
    try:
        with open(SCHOLARSHIPS_FILE, "r", encoding = "utf-8") as f:
            reader = csv.reader(f)
            for row in reader: #reads each row
                scholarships.append(row) #appends each row to the list
    except FileNotFoundError as e:
        print("Scholarships file not found:", e)


def save_scholarships():
    """
    saves scholarships to scholarships.csv
    """
    with open(SCHOLARSHIPS_FILE, "w", encoding = "utf-8", newline="") as f:
        writer = csv.writer(f)
        for newscholarship in scholarships: #iterate throught scholarships list
            writer.writerow(newscholarship) #write each scholarship to the list
