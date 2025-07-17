# Task 3: Count vowels in a string

def count_vowels(text):
    """
    Count total vowels and each vowel in the given text.
    """
    vowels = 'aeiou'                # String of vowels to check
    text_lower = text.lower()       # Convert text to lowercase for case-insensitive counting
    total = 0                       # Initialize total vowel count
    counts = {}                     # Dictionary to store count of each vowel
    for v in vowels:                # Loop through each vowel
        count = text_lower.count(v) # Count occurrences of the vowel
        counts[v] = count           # Store in dictionary
        total += count              # Add to total
    print(f"Total vowels: {total}") # Print total number of vowels
    for v in vowels:                # Loop again to print each vowel's count
        print(f"{v}: {counts[v]}")

# Test the function with the given string
sample_text = "Torture the data, and it will confess to anything."  # Provided string
count_vowels(sample_text)  # Call the function 