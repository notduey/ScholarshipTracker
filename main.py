#!/usr/bin/env python
"""
main file for scholarship tracker
"""
from menu import main_menu
from data import load_scholarships, save_scholarships


def main():
    """
    main function
    """
    load_scholarships()
    main_menu()
    save_scholarships()


if __name__ == "__main__":
    main()
