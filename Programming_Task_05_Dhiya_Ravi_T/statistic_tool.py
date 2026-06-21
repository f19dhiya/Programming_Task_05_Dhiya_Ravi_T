def main():
    numbers = []
    count = 10

    print("=== Number Statistics Tool ===")
    for i in range(count):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = sum(1 for n in numbers if n % 2 != 0)

    print("\n--- Results ---")
    print(f"Largest Number: {largest}")
    print(f"Smallest Number: {smallest}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Even Numbers: {even_count}")
    print(f"Odd Numbers: {odd_count}")


if __name__ == "__main__":
    main()