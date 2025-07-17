# Task 5: Customer purchase totals

purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]  # Example data
customer_totals = {}  # Dictionary to store totals per customer
for name, amount in purchases:  # Loop through each purchase
    if name in customer_totals:  # If customer already in dictionary
        customer_totals[name] += amount  # Add to their total
    else:
        customer_totals[name] = amount   # Otherwise, start their total
for name, total in customer_totals.items():  # Loop through dictionary
    print(f"{name} spent ${total}")  # Print total spent per customer 