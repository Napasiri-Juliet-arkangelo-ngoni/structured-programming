def main():
    """
    """
    numbers = []

    print("Enter 5 numbers:")
    for i in range(5):
        while True:
            try:
# Enter any number
                num_str = input(f"Enter number {i + 1}: ")
                num = int(num_str)
                numbers.append(num)  
                break  
            except ValueError:
                print("Invalid input. Please enter an integer.")
    print(f"\nNumbers: {numbers}")
    if numbers:  
        maximum = max(numbers)
        minimum = min(numbers)
        average = sum(numbers) / len(numbers)

        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
        print(f"Average: {average:.1f}")
    else:
        print("No numbers were entered to calculate statistics.")
    sorted_numbers = sorted(numbers)
    print(f"Sorted: {sorted_numbers}")
if __name__ == "__main__":
    main()