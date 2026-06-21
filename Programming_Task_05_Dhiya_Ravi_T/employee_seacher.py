def search_employee(employees, name):
    for employee in employees:
        if employee.lower() == name.lower():
            return True
    return False


def main():
    employees = ["John", "Alice", "David", "Sophia", "Michael"]

    print("=== Employee Record Search ===")
    print("Employee Records:", employees)

    search_name = input("\nEnter the name to search: ").strip()

    if search_employee(employees, search_name):
        print("Record Found")
    else:
        print("Record Not Found")


if __name__ == "__main__":
    main()