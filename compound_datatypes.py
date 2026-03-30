# fruits = ['apple', 'banana', 'cherry', 'date']
# fruits.append('elderberry')
# fruits.remove('banana')
# fruits.sort()
# print(fruits)

# student = {'name': 'john Doe', 'age': 25 ,
#          'major': 'Computer Science',
#         }

# student['major'] = "Electrical Engineering"
# student["year"] = "Senior"

# print(student.keys())
# print(student.values())

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

print("Second book title:", books[1]["title"])

print("Third book year:", books[2]["year"])

print("\nBook List:")
for book in books:
    print(f"{book['title']} by {book['author']}")

    courses = {
    "math": ["Alice", "Bob", "Charlie"],
    "history": ["David", "Emma", "Frank"],
    "chemistry": ["Grace", "Henry", "Isabella"]
}

courses["math"].extend(["Jack", "Karen", "Liam", "Mia", "Noah"])

courses["history"].pop(2)

print("\nChemistry students:", courses["chemistry"])

courses["physics"] = ["Olivia", "Paul", "Quinn", "Ryan"]

print("\nUpdated Courses:")
for course, students in courses.items():
    print(f"{course}: {students}")