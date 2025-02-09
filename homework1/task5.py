"""
Create a new file named task5.py and inside create a list of of your
favorite books, including book titles and authors. Use list slicing 
to print the first three books in the list. Create a dictionary that
represents a basic student database, including student names and their 
corresponding student IDs. Implement pytest test cases to verify the 
correctness of your code for each data structure.
"""

favorite_books = [
    "A Scanner Darkly",
    "House of Leaves",
    "Blood Meridian",
    "Siddhartha",
    "On the Shortness of Life",
]

students = {
    "Philip": 12345,
    "Mark": 67890,
    "Cormack": 58372,
    "Hermann": 83475,
    "Seneca": 87374,
}

def get_first_three_favorite_books():
    return favorite_books[:3]

def get_students():
    return students