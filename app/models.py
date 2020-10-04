import enum

from database import Base
from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

periodicitys = ('weekly', 'daily', 'monthly', 'yearly')
periodicity_enum = Enum(*periodicitys, name='periodicity')


services = ('speech', 'OT', 'PT')
service_enum = Enum(*services, name="service")

names = ('provider', 'supervisor', 'principal', 'admin', 'seeall')
name_enum = Enum(*names, name="name_enum")


counties = ('Q', 'M', 'R',
            'X', 'K')
counties_enum = Enum(*counties, name='county_enum')


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)
    #first_name = Column(String)
    #last_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean)

    roles = relationship("Role", back_populates="user")

    caseloads = relationship("Caseload", back_populates="user")


class School(Base):
    __tablename__ = "school"

    id = Column(String, primary_key=True)

    district = Column(String)
    county = Column(counties_enum)
    name = Column(String)

    students = relationship("Student", back_populates="school")


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)

    first_name = Column(String)
    last_name = Column(String)
    osis = Column(String)
    birthdate = Column(Date)
    grade = Column(String)

    school_id = Column(String, ForeignKey('school.id'))
    school = relationship("School", back_populates="students")

    ieps = relationship("Iep", back_populates="student")

    cases = relationship("Case", back_populates="student")


class Iep(Base):
    __tablename__ = 'iep'

    id = Column(Integer, primary_key=True)

    start_date = Column(Date)
    end_date = Column(Date)

    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", back_populates="ieps")

    mandates = relationship('Mandate', back_populates='iep')

    goals = relationship('Goal', back_populates='iep')


class Mandate(Base):
    __tablename__ = 'mandate'

    id = Column(Integer, primary_key=True)

    service = Column(service_enum)
    group_size = Column(Integer)
    duration = Column(Integer)
    periodicity = Column(periodicity_enum)
    frequency = Column(Integer)
    interval = Column(Integer)

    iep_id = Column(Integer, ForeignKey('iep.id'))
    iep = relationship("Iep", back_populates="mandates")


class Goal(Base):
    __tablename__ = 'goal'

    id = Column(Integer, primary_key=True)

    goal = Column(String)
    criteria = Column(String)
    method = Column(String)
    schedule = Column(String)

    iep_id = Column(Integer, ForeignKey('iep.id'))
    iep = relationship("Iep", back_populates="goals")


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)

    name = Column(name_enum)
    school = Column(String)
    district = Column(String)
    county = Column(counties_enum)
    service = Column(service_enum)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="roles")


class Caseload(Base):
    __tablename__ = 'caseload'

    id = Column(Integer, primary_key=True)

    title = Column(String)
    service = Column(service_enum)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="caseloads")

    cases = relationship("Case", back_populates="caseload")


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)

    caseload_id = Column(Integer, ForeignKey('caseload.id'))
    caseload = relationship("Caseload", back_populates="cases")

    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", back_populates="cases")
