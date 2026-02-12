# ScholarshipTracker
A modular Python console application for tracking scholarships, built from scratch as my first full-scale Python project. Light AI assistence was used for program structure and sanity checks!

This program allows users to add, view, edit, and delete scholarships, with persistent storage using a CSV file. It emphasizes clean structure, strong input validation, and real-world usability.

## OverviewSkills
- ScholarshipTracker is a command-line application that manages scholarship data including:

- Name

- Link

- Award amount

- Application deadline

- Completion status (Incomplete / Ongoing / Complete)

- Essay requirement

- Additional notes

- All data is stored in scholarships.csv to ensure persistence across sessions.

This project was built over ~3 weeks with minimal AI assistance (mainly for structuring and sanity checks). All core logic, validation systems, and program flow were implemented by me.

## Features
- Add Scholarships

Optional and required fields

Default amount handling

Date validation (MM/DD/YYYY format)

Essay requirement toggle (Y/N)

Graceful input handling

- View Scholarships

Clean formatted output

Currency formatting

Human-readable dates (e.g., "February 11, 2026")

Status clearly displayed

Notes included

- Edit Scholarships

Field-by-field editing menu

Cancelable edits

Robust date re-validation

Status updates

Real-time feedback

- Delete Scholarships

Selection by index

Confirmation prompt before deletion

Safe handling of invalid selections

- Persistent Storage

CSV-based file storage

Automatic load on program start

Save and exit functionality

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

## How to Run

1. Make sure python is installed
2. Clone the Repository:
```bash
git clone https://github.com/yourusername/ScholarshipTracker.git
```
3. Navigate into the directory:
```bash
cd ScholarshipTracker
```
4. Run the program in terminal:
```bash
python main.py
```