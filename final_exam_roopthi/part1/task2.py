# Task 2: Define a function to check grades

def check_grades(grades):
    """
    For each grade in the list, print 'Pass' if grade >= 75, else 'No'.
    """
    for grade in grades:           # Loop through each grade in the list
        if grade >= 75:            # Check if the grade is 75 or more
            print("Pass")          # Print 'Pass' if condition is met
        else:
            print("No")            # Print 'No' otherwise

# Test the function with a sample list
sample_grades = [80, 74, 90, 60, 77]  # Example list of 5 grades
check_grades(sample_grades)           # Call the function 