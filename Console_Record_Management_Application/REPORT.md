# Assignment 1 – Mini Project
# Console Record-Management Application

## 1. Introduction

The Console Record-Management Application is a Python-based mini project developed to demonstrate fundamental programming concepts through a practical application.

The project implements a Student Record Management System. It allows the user to perform common record-management operations such as adding, viewing, searching, updating, and deleting student records.

The application runs entirely in the console and uses a JSON file for permanent storage. This ensures that records are not lost when the program is closed.

---

## 2. Objectives

The main objectives of this project are:

1. To develop a functional menu-driven Python application.
2. To apply Python data types and variables in a practical program.
3. To use conditional statements and loops.
4. To divide the program into reusable functions.
5. To handle invalid input and runtime errors using exception handling.
6. To implement File I/O for permanent data storage.
7. To demonstrate CRUD operations:
   - Create
   - Read
   - Update
   - Delete
8. To maintain clean, readable, and modular source code.

---

## 3. Problem Statement

Managing student information manually can become difficult when the number of records increases. A simple computerized system can make these operations easier.

The proposed application provides a console-based solution where a user can maintain student records using a simple menu. The system stores the records in a JSON file so that the information remains available between program executions.

---

## 4. Scope of the Project

The project is designed for small-scale record management.

### Included
- Adding student records
- Displaying records
- Searching records
- Updating records
- Deleting records
- Persistent storage
- Input validation
- Error handling

### Not Included
- User login/authentication
- Database server
- Graphical user interface
- Network or cloud storage
- Multiple user accounts

These features could be added in future versions.

---

## 5. Technologies Used

| Technology / Concept | Purpose |
|---|---|
| Python 3 | Main programming language |
| JSON | Persistent record storage |
| pathlib | File and directory handling |
| Lists | Collection of records |
| Dictionaries | Individual record structure |
| Functions | Modular program design |
| Loops | Repeated menu and record operations |
| Conditional statements | Decision making |
| Exception handling | Handling invalid input and file errors |
| File I/O | Reading and writing records |

---

## 6. Data Types and Data Structures

The application uses several Python data types.

### Integer
Used for student ID and age.

Example:
```python
record_id = 101
age = 21
```

### String
Used for name, course, email, and phone number.

Example:
```python
name = "Rahul Sharma"
course = "BSc Computer Science"
```

### List
All student records are stored in a list.

Example:
```python
records = []
```

### Dictionary
Each student record is represented by a dictionary.

Example:
```python
{
    "id": 101,
    "name": "Rahul Sharma",
    "age": 21,
    "course": "BSc Computer Science",
    "email": "rahul@example.com",
    "phone": "9876543210"
}
```

---

## 7. Application Design

The application follows a menu-driven design.

### Main Menu

```text
1. Add Record
2. View Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
```

The user selects an operation and the corresponding function is called.

After the operation is completed, the menu is displayed again until the user selects Exit.

---

## 8. Functional Modules

### 8.1 Add Record

The `add_record()` function collects information from the user and creates a dictionary.

Before adding the record, the program checks whether the entered ID already exists.

The record is then appended to the list and saved to the JSON file.

### 8.2 View Records

The `view_records()` function displays all available records.

If the list is empty, an appropriate message is shown.

### 8.3 Search Record

The `search_records()` function supports:

- Search by student ID
- Search by student name

Name searches are case-insensitive and can also match part of a name.

### 8.4 Update Record

The `update_record()` function searches for a record by ID and allows the user to change its information.

Pressing Enter without entering a new value keeps the existing value.

### 8.5 Delete Record

The `delete_record()` function identifies a record by ID and asks for confirmation before deleting it.

### 8.6 File Handling

The application uses the JSON file:

```text
data/records.json
```

The following operations are performed:

- Read records when the application starts
- Write records after add/update/delete operations
- Create the data file automatically if it does not exist

---

## 9. Exception Handling

Exception handling is used to prevent the application from crashing because of invalid input or file errors.

For example:

```python
try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("Invalid input.")
```

File-related exceptions are also handled, including:

- `FileNotFoundError`
- `JSONDecodeError`
- `OSError`

This improves application reliability.

---

## 10. Use of Loops and Conditional Statements

The main application uses a `while` loop to repeatedly display the menu.

A `for` loop is used to display records.

Conditional statements are used to identify the user's menu choice:

```python
if choice == 1:
    add_record(records)
elif choice == 2:
    view_records(records)
...
```

This demonstrates decision-making and repetition in Python.

---

## 11. Program Flow

```text
Start
  |
  v
Load records from JSON file
  |
  v
Display main menu
  |
  +----> Add Record ----> Save file
  |
  +----> View Records
  |
  +----> Search Record
  |
  +----> Update Record ----> Save file
  |
  +----> Delete Record ----> Save file
  |
  +----> Exit
  |
  v
End
```

---

## 12. Source Code Structure

The project uses a single main Python file for simplicity.

```text
main.py
```

Important functions include:

- `ensure_data_file()`
- `load_records()`
- `save_records()`
- `display_record()`
- `get_non_empty()`
- `get_positive_integer()`
- `find_record()`
- `add_record()`
- `view_records()`
- `search_records()`
- `update_record()`
- `delete_record()`
- `show_menu()`
- `main()`

This structure keeps individual responsibilities separated and makes the program easier to understand and maintain.

---

## 13. Testing

The application should be tested using normal and invalid inputs.

| Test Case | Input / Action | Expected Result |
|---|---|---|
| Add record | Valid student details | Record added |
| Duplicate ID | Existing ID | Duplicate record rejected |
| View records | Select option 2 | All records displayed |
| Search by ID | Existing ID | Matching record displayed |
| Search by name | Existing name | Matching record displayed |
| Search invalid ID | Non-existing ID | Not found message |
| Update record | Existing ID | Record updated |
| Delete record | Existing ID + y | Record deleted |
| Invalid menu input | Text such as `abc` | Error message displayed |
| Invalid age | Text instead of number | Error message displayed |
| Empty name | Press Enter | Input requested again |
| Empty records | View before adding | No records message |

---

## 14. Sample Output

### Adding a Record

```text
--- Add Record ---
Enter student ID: 101
Enter student name: Rahul Sharma
Enter age: 21
Enter course: BSc Computer Science
Enter email: rahul@example.com
Enter phone number: 9876543210
Record added successfully.
```

### Viewing Records

```text
--- View Records ---

Total records: 1
--------------------------------------------------
ID      : 101
Name    : Rahul Sharma
Age     : 21
Course  : BSc Computer Science
Email   : rahul@example.com
Phone   : 9876543210
--------------------------------------------------
```

### Invalid Input

```text
Enter your choice (1-6): abc
Invalid input. Please enter a number from 1 to 6.
```

---

## 15. Advantages

1. Simple and easy-to-use console interface.
2. Data is stored permanently.
3. No external Python packages are required.
4. Modular functions improve readability.
5. Input validation reduces invalid data.
6. Exception handling prevents common runtime failures.
7. The project demonstrates multiple Python concepts in one application.

---

## 16. Limitations

1. The application is console-based.
2. It does not have user authentication.
3. It is intended for small-scale data management.
4. JSON file storage is not suitable for very large datasets.
5. Multiple users cannot safely modify the file simultaneously.

---

## 17. Future Enhancements

Possible future improvements include:

- Graphical User Interface using Tkinter
- SQLite/MySQL database integration
- Login and authentication
- Sorting and filtering
- Export to CSV
- Input validation for email and phone formats
- Backup and restore functionality
- Student attendance and marks modules

---

## 18. Conclusion

The Console Record-Management Application successfully demonstrates the major Python concepts required for Assignment 1.

The project combines data types, variables, conditional statements, loops, functions, exception handling, and File I/O into one practical application.

The menu-driven structure allows users to perform complete CRUD operations on student records. JSON-based storage ensures that records remain available after the application is closed.

The project therefore provides a simple but complete example of how fundamental Python programming concepts can be integrated into a working real-world style application.

---

## 19. GitHub Submission Checklist

Before submitting the GitHub repository, verify that it contains:

- [ ] `main.py`
- [ ] `README.md`
- [ ] `REPORT.md`
- [ ] `requirements.txt`
- [ ] `data/records.json`
- [ ] Screenshots of the working application
- [ ] Clear repository name and description
- [ ] Clean folder structure
- [ ] Working code tested locally
- [ ] GitHub repository link ready for submission
