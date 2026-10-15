"""
THDC-IHET Python Fundamentals Practice
Run with: python main.py
"""

# 1. Variables and data types
student_name = "Student"
student_year = 2
python_score = 82.5
completed_setup = True

print("=== 1. Variables and Data Types ===")
print("Name:", student_name, "| Type:", type(student_name).__name__)
print("Year:", student_year, "| Type:", type(student_year).__name__)
print("Score:", python_score, "| Type:", type(python_score).__name__)
print("Setup complete:", completed_setup, "| Type:", type(completed_setup).__name__)

# 2. Conditional statements
print("\n=== 2. Conditions ===")
score = 82
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Needs improvement"
print(f"Score {score} -> Grade {grade}")

# 3. Loops
print("\n=== 3. Loops ===")
for number in range(1, 6):
    print(number, end=" ")
print()
countdown = 3
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1

# 4. Functions
print("\n=== 4. Functions ===")
def calculate_average(numbers):
    """Return the arithmetic mean, or None for an empty list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print("Average:", calculate_average([70, 80, 90]))

# 5. Python data structures
print("\n=== 5. Data Structures ===")
skills = ["Python", "Git", "SQL"]                 # list
student = {"name": "Student", "year": 2}          # dictionary
unique_scores = {70, 80, 80, 90}                  # set
coordinates = (30.3, 78.0)                        # tuple
print("List:", skills)
print("Dictionary:", student)
print("Set (duplicates removed):", unique_scores)
print("Tuple:", coordinates)

# 6. Basic searching
print("\n=== 6. Searching ===")
def linear_search(items, target):
    """Return the index of target, or -1 if it is absent."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

values = [12, 5, 19, 7, 3]
print("Values:", values)
print("Index of 19:", linear_search(values, 19))
print("Index of 100:", linear_search(values, 100))

# 7. Basic sorting (bubble sort)
def bubble_sort(items):
    """Return a sorted copy using bubble sort."""
    result = items.copy()
    n = len(result)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result

print("\n=== 7. Sorting ===")
print("Original:", values)
print("Bubble sorted:", bubble_sort(values))

# 8. Easy practice problems
print("\n=== 8. Practice Problems ===")
def is_even(number):
    return number % 2 == 0

def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for character in text.lower() if character in vowels)

def find_largest(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

print("Is 14 even?", is_even(14))
print("Vowels in 'Python programming':", count_vowels("Python programming"))
print("Largest value:", find_largest([4, 18, 2, 11]))

print("\nAll practice examples executed successfully.")
