# Task 4: Data collection tool (user input)

numbers = []  # List to store user-entered numbers
while True:  # Infinite loop to keep asking for input
    user_input = input("Enter a number (or 'done' to finish): ")  # Prompt user
    if user_input.strip().lower() == 'done':  # If user types 'done' (case-insensitive)
        break  # Exit the loop
    if user_input.strip() == '':  # Skip empty input
        print("Invalid input. Try again.")
        continue  # Go to next iteration
    try:
        num = float(user_input)  # Try to convert input to a float
        numbers.append(num)      # Add to the list
    except ValueError:
        print("Invalid input. Try again.")  # If not a number, show error

if numbers:  # If the list is not empty
    print(f"Total numbers entered: {len(numbers)}")  # Print how many numbers
    avg = sum(numbers) / len(numbers)  # Calculate average
    print(f"Average: {avg:.2f}")       # Print average rounded to 2 decimals
else:
    print("No valid numbers entered.") 