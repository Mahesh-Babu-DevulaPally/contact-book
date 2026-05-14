Contact Book Management System

A Python-based Contact Book application with a graphical user interface built using Tkinter. This application allows users to store, manage, search, update, and delete contacts efficiently using file-based storage.

Overview

This Contact Book application helps users organize phone contacts through a simple desktop interface. It supports multiple phone numbers for a single contact, contact searching, updating, deletion, and automatic data persistence using text files.

Features
Simple GUI Interface: User-friendly desktop application built with Tkinter
Add Contacts: Store contact names and phone numbers
Multiple Numbers Support: Save multiple phone numbers for the same contact
Search by Name: Find contacts quickly using names
Search by Phone Number: Identify contact owners using phone numbers
Update Contacts: Add additional numbers to existing contacts
Delete Contacts: Remove contacts or specific phone numbers
Display All Contacts: View all saved contacts in alphabetical order
File-Based Storage: Contacts are stored permanently in a text file
Input Validation: Validates names and phone numbers using regular expressions
Duplicate Detection: Prevents duplicate phone numbers for the same contact

HOW IT WORKS
Input Phase

Users enter:

Contact name
Phone number

through the graphical interface.

Contact Storage

The application stores contacts in:

contacts.txt

Each contact is saved in:

Name,PhoneNumber
format.

Contact Management

Users can:

Add new contacts
Update existing contacts
Delete contacts
Search contacts
Search Functionality

The application supports:

Search by contact name
Search by phone number
Display Contacts

All contacts are displayed alphabetically in a separate window.

nstallation

Clone or download the repository.

No external libraries are required because all modules used are built into Python.

Run the application:

python contact_book.py
Usage
Launch the Application

Run the Python file to open the GUI.

Add Contact

Enter:

Name
10-digit phone number

Then click:

Add Contact
Search Contact

Use:

Search By Name
Search By Phone

to find saved contacts.

Update Contact

Enter an existing contact name and a new phone number to add additional numbers.

Delete Contact

Enter contact details and remove unwanted numbers.

Display Contacts

Click:

Display Contacts

to view all saved contacts.

Technical Details
GUI Framework

Library Used: Tkinter

The interface includes:

Labels
Entry fields
Buttons
Popup windows
Text display area
File Handling

Contacts are stored locally using:

open()

operations with automatic loading and saving functionality.

Regular Expressions

Regex validation ensures:

Names contain only alphabets and spaces
Phone numbers contain exactly 10 digits

Input Validation

Prevents empty inputs
Validates phone number length
Ensures proper name formatting
Removes extra spaces
Detects duplicate phone numbers

Error Handling

Handles missing contact files
Prevents duplicate entries
Displays user-friendly warning messages
Handles invalid search operations gracefully

Limitations

Uses text-file storage instead of databases
Desktop application only
Supports only 10-digit phone numbers
No cloud synchronization

Future Enhancements

Database integration using SQLite/MySQL
Contact profile pictures
Import/Export contacts
Dark mode support
Email field integration
Search filtering and sorting
Mobile number validation with country codes

Contributing

Contributions are welcome!
Feel free to submit pull requests or open issues for bug fixes and feature improvements.