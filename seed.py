from faker import Faker
from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade
import random

fake = Faker()
db = SessionLocal()

# Створюємо групи
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
db.add_all(groups)
db.commit()

# Створюємо викладачів
teachers = [Teacher(fullname=fake.name()) for _ in range(4)]
db.add_all(teachers)
db.commit()

# Створюємо предмети
subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(6)]
db.add_all(subjects)
db.commit()

# Створюємо студентів
students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(40)]
db.add_all(students)
db.commit()

# Додаємо оцінки
for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            db.add(Grade(student=student, subject=subject, grade=random.uniform(60, 100)))
db.commit()

db.close()
