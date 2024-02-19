my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

def get_student_info(data, user_id):
    student = next((s for s in data['students'] if s['id'] == user_id), None)

    if student:
        print(f"Student information:\nID: {student['id']}, Name: {student['name'].capitalize()}, Age: {student['age']}")
        
        student_grades = {}
        for subject in data['subjects']:
            grade = subject['grades'].get(str(user_id), 'N/A')
            student_grades[subject['name']] = grade

        for subject, grade in student_grades.items():
            print(f"Subject: {subject}, Grade: {grade}")
    else:
        print(f"Student with ID {user_id} not found.")

user_id_input = int(input("Enter student ID: "))

get_student_info(my_dict, user_id_input)





