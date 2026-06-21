def main():
    marks = []
    num_students = 5

    print("=== Student Marks Analyzer ===")
    for i in range(num_students):
        while True:
            try:
                mark = int(input(f"Enter marks for Student {i + 1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    print("\n--- Results ---")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")


if __name__ == "__main__":
    main()