"""
Console Record-Management Application
Mini Project - Assignment 1

A menu-driven Student Record Management System using:
- Data types and variables
- Conditional statements and loops
- Functions
- Exception handling
- File I/O (JSON)
"""

import json
from pathlib import Path

DATA_FILE = Path("data/records.json")


def ensure_data_file():
    """Create the data directory and JSON file if they do not exist."""
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not DATA_FILE.exists():
            DATA_FILE.write_text("[]", encoding="utf-8")
    except OSError as error:
        print(f"Error creating data file: {error}")


def load_records():
    """Load records from the JSON file."""
    ensure_data_file()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            print("Invalid data format. Starting with an empty record list.")
            return []

        return records

    except FileNotFoundError:
        print("Data file was not found. A new file will be created.")
        return []
    except json.JSONDecodeError:
        print("Data file contains invalid JSON. Starting with an empty list.")
        return []
    except OSError as error:
        print(f"Error reading records: {error}")
        return []


def save_records(records):
    """Save all records to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        return True
    except OSError as error:
        print(f"Error saving records: {error}")
        return False


def display_record(record):
    """Display one record in a readable format."""
    print("-" * 50)
    print(f"ID      : {record['id']}")
    print(f"Name    : {record['name']}")
    print(f"Age     : {record['age']}")
    print(f"Course  : {record['course']}")
    print(f"Email   : {record['email']}")
    print(f"Phone   : {record['phone']}")


def get_non_empty(prompt):
    """Get a non-empty string from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def find_record(records, record_id):
    """Return a record matching the given ID, or None."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def add_record(records):
    """Add a new student record."""
    print("\n--- Add Record ---")
    record_id = get_positive_integer("Enter student ID: ")

    if find_record(records, record_id) is not None:
        print("A record with this ID already exists.")
        return

    name = get_non_empty("Enter student name: ")
    age = get_positive_integer("Enter age: ")
    course = get_non_empty("Enter course: ")
    email = get_non_empty("Enter email: ")
    phone = get_non_empty("Enter phone number: ")

    new_record = {
        "id": record_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "phone": phone
    }

    records.append(new_record)

    if save_records(records):
        print("Record added successfully.")


def view_records(records):
    """Display all records."""
    print("\n--- View Records ---")

    if not records:
        print("No records available.")
        return

    print(f"\nTotal records: {len(records)}")
    for record in records:
        display_record(record)
    print("-" * 50)


def search_records(records):
    """Search records by ID or name."""
    print("\n--- Search Records ---")

    if not records:
        print("No records available.")
        return

    print("1. Search by ID")
    print("2. Search by Name")

    try:
        choice = int(input("Enter your choice: ").strip())
    except ValueError:
        print("Invalid choice. Please enter 1 or 2.")
        return

    matches = []

    if choice == 1:
        record_id = get_positive_integer("Enter student ID: ")
        record = find_record(records, record_id)
        if record:
            matches.append(record)
    elif choice == 2:
        keyword = get_non_empty("Enter name or part of name: ").lower()
        matches = [
            record for record in records
            if keyword in record["name"].lower()
        ]
    else:
        print("Invalid choice.")
        return

    if not matches:
        print("No matching record found.")
        return

    print(f"\nFound {len(matches)} record(s):")
    for record in matches:
        display_record(record)
    print("-" * 50)


def update_record(records):
    """Update an existing record."""
    print("\n--- Update Record ---")

    if not records:
        print("No records available.")
        return

    record_id = get_positive_integer("Enter student ID to update: ")
    record = find_record(records, record_id)

    if record is None:
        print("Record not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{record['name']}]: ").strip()
    age_input = input(f"Age [{record['age']}]: ").strip()
    course = input(f"Course [{record['course']}]: ").strip()
    email = input(f"Email [{record['email']}]: ").strip()
    phone = input(f"Phone [{record['phone']}]: ").strip()

    if name:
        record["name"] = name

    if age_input:
        try:
            age = int(age_input)
            if age <= 0:
                print("Age must be greater than 0. Existing age retained.")
            else:
                record["age"] = age
        except ValueError:
            print("Invalid age. Existing age retained.")

    if course:
        record["course"] = course
    if email:
        record["email"] = email
    if phone:
        record["phone"] = phone

    if save_records(records):
        print("Record updated successfully.")


def delete_record(records):
    """Delete a record after confirmation."""
    print("\n--- Delete Record ---")

    if not records:
        print("No records available.")
        return

    record_id = get_positive_integer("Enter student ID to delete: ")
    record = find_record(records, record_id)

    if record is None:
        print("Record not found.")
        return

    display_record(record)

    confirmation = input("Are you sure you want to delete this record? (y/n): ").strip().lower()

    if confirmation == "y":
        records.remove(record)
        if save_records(records):
            print("Record deleted successfully.")
    else:
        print("Delete operation cancelled.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("       STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("=" * 50)


def main():
    """Run the application."""
    records = load_records()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-6): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            add_record(records)
        elif choice == 2:
            view_records(records)
        elif choice == 3:
            search_records(records)
        elif choice == 4:
            update_record(records)
        elif choice == 5:
            delete_record(records)
        elif choice == 6:
            print("Thank you for using the Student Record Management System.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
