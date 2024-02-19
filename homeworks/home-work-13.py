# შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,marks
# 1,string,0,string,string,0
# 2,string,0,string,string,0


# დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას (id,name,age,grade,subject_name,marks)
# და თქვენ სტუდენტს დაამატებთ csv ფაილში.

# დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის 
# ინფომრაციის წაკითხვა ფაილიდან.

# დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს
# სტუდენტის აიდს, საგანს და განახლებულ ქულას.


import csv
import os

csv_file_path = "students.csv"

def create_csv():
    header = ["id", "name", "age", "grade", "subject_name", "marks"]
    
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def add_student_info(id, name, age, grade, subject_name, marks):
    data = [id, name, age, grade, subject_name, marks]

    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_all_students():
    with open(csv_file_path, mode='r') as file:
        reader = list(csv.reader(file))
        for row in reader:
            print(row)

def read_student_by_id(student_id):
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == str(student_id):
                print(row)
                return

    print(f"Student with ID {student_id} not found.")

def update_student_grade(student_id, subject_name, updated_grade):
    rows = []

    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == str(student_id) and row[4] == subject_name:
                row[3] = updated_grade
            rows.append(row)

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

if not os.path.exists(csv_file_path):
    create_csv()

add_student_info(1, "John", 20, "A", "Math", 90)
add_student_info(2, "Alice", 22, "B", "Physics", 85)

read_all_students()
read_student_by_id(2)

update_student_grade(1, "Math", "B")

print("\nAfter updating grade:")
read_all_students()
