from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc
from database import engine
from models import Student, Grade, Subject, Teacher, Group

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    """5 студентів із найбільшим середнім балом з усіх предметів"""
    return session.query(
        Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    """Студент із найвищим середнім балом з певного предмета"""
    return session.query(
        Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(subject_name):
    """Середній бал у групах з певного предмета"""
    return session.query(
        Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group.id).all()

def select_4():
    """Середній бал на потоці"""
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(teacher_name):
    """Які курси читає певний викладач"""
    return session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()

def select_6(group_name):
    """Список студентів у певній групі"""
    return session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    """Оцінки студентів у окремій групі з певного предмета"""
    return session.query(Student.fullname, Grade.grade).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(teacher_name):
    """Середній бал, який ставить певний викладач зі своїх предметів"""
    return session.query(func.round(func.avg(Grade.grade), 2)).join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).scalar()

def select_9(student_name):
    """Список курсів, які відвідує студент"""
    return session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).distinct().all()

def select_10(student_name, teacher_name):
    """Список курсів, які певному студенту читає певний викладач"""
    return session.query(Subject.name).join(Grade).join(Student).join(Teacher).filter(Student.fullname == student_name, Teacher.fullname == teacher_name).all()
