# ScholarshipTracker
A modular Python console application for tracking scholarships, built from scratch as my first full-scale Python project. Light AI assistence was used for program structure and sanity checks!

This program allows users to add, view, edit, and delete scholarships, with persistent storage using a CSV file. It emphasizes clean structure, strong input validation, and real-world usability.

## Overview
- ScholarshipTracker is a command-line application that manages scholarship data including:

- Name

- Link

- Award amount

- Application deadline

- Completion status (Incomplete / Ongoing / Complete)

- Essay requirement

- Additional notes

- All data is stored in scholarships.csv to ensure persistence across sessions.

This project was built over ~3 weeks with minimal AI assistance (mainly for structuring and sanity checks). All core logic, validation systems, and program flow were implemented by me. A bunch of my time in this project was spent on making sure invalid user inputs were handled safely so the program wouldn't crash or data wouldn't get messed up!

## How to Run

1. Make sure Python is installed (Python 3.8 or later)
2. Clone the Repository:
SSH
```bash
git clone git@github.com:notduey/ScholarshipTracker.git
```
HTTPS
```bash
git clone https://github.com/yourusername/ScholarshipTracker.git
```
3. Navigate into the directory:
```bash
cd .../.../ScholarshipTracker
```
4. Run the program in terminal:
Windows
```bash
python main.py
```
MacOS
```bash
python3 main.py

```

## Project Structure

```bash
ScholarshipTracker/
│
├── main.py
├── menu.py
├── data.py
├── add_edit_scholarship.py
├── add_edit_functions.py
├── manage_scholarship.py
├── view_scholarship.py
├── scholarships.csv
└── README.md
```
Module Responsibilities

- main.py – Program entry point

- menu.py – Main navigation logic

- data.py – CSV file loading/saving

- add_edit_scholarship.py – Scholarship creation logic

- add_edit_functions.py – Reusable validation utilities

- manage_scholarship.py – Edit/Delete operations

- view_scholarship.py – Formatting and display logic