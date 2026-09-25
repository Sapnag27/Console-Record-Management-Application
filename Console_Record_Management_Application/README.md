# Console Record-Management Application

## Project Title
**Student Record Management System – Console Application**

## Project Description
This mini project is a Python-based console application for managing student records. It provides a menu-driven interface through which users can add, view, search, update, and delete records.

Records are stored permanently in a JSON file using Python File I/O. Therefore, data remains available even after the application is closed.

## Features
- Add a new student record
- View all student records
- Search records by ID or name
- Update an existing record
- Delete a record with confirmation
- Automatic JSON file creation
- Persistent data storage
- Input validation
- Exception handling for invalid input and file errors
- Function-based modular program structure
- Menu-driven console interface

## Technologies / Python Concepts Used
- Python 3
- Variables and data types
- Lists and dictionaries
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions
- Exception handling (`try`, `except`)
- File I/O (`open`, `read`, `write`)
- JSON data storage
- `pathlib.Path`

## Project Structure

```text
Console_Record_Management_Application/
│
├── main.py
├── README.md
├── REPORT.md
├── requirements.txt
├── data/
│   └── records.json
└── screenshots/
    └── README.md
```

## How to Run

### 1. Install Python
Install Python 3.x from the official Python website if it is not already installed.

### 2. Clone the repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Console_Record_Management_Application
```

### 3. Run the application
```bash
python main.py
```

On some systems:
```bash
python3 main.py
```

No third-party packages are required.

## Sample Input / Output

```text
==================================================
       STUDENT RECORD MANAGEMENT SYSTEM
==================================================
1. Add Record
2. View Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
==================================================
Enter your choice (1-6): 1

--- Add Record ---
Enter student ID: 101
Enter student name: Rahul Sharma
Enter age: 21
Enter course: BSc Computer Science
Enter email: rahul@example.com
Enter phone number: 9876543210
Record added successfully.
```

Example search:

```text
--- Search Records ---
1. Search by ID
2. Search by Name
Enter your choice: 1
Enter student ID: 101

Found 1 record(s):
--------------------------------------------------
ID      : 101
Name    : Rahul Sharma
Age     : 21
Course  : BSc Computer Science
Email   : rahul@example.com
Phone   : 9876543210
--------------------------------------------------
```

## Data Storage
The application stores records in:

`data/records.json`

Example:

```json
[
    {
        "id": 101,
        "name": "sapna gupta",
        "age": 21,
        "course": "BSc Computer Science",
        "email": "sapna@example.com",
        "phone": "9876543210"
    }
]
```

## Screenshots
Add screenshots of the running application to the `screenshots/` folder before final submission. Recommended screenshots:
1. Main menu
2. Add record
3. View records
4. Search record
5. Update record
6. Delete record
7. Invalid input / exception handling

## GitHub Repository Details
**Repository Name:** `Console-Record-Management-Application`

**Repository URL:** Replace this line with your actual GitHub repository link after uploading the project.

## Author
Student Mini Project – Assignment 1
