from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))
    
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False, unique=True)
    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    grade = Column(Float, nullable=False)
    date_received = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
