import enum

from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

periodicitys = ('weekly', 'daily', 'monthly', 'yearly')
periodicity_enum = Enum(*periodicitys, name='periodicity')


services = ('speech', 'OT', 'PT')
service_enum = Enum(*services, name="service")

roles = ('provider', 'supervisor', 'principal', 'admin', 'seeall')
role_enum = Enum(*roles, name="role_enum")


counties = ('Q', 'M', 'R',
            'X', 'K')

counties_enum = Enum(*counties, name='county_enum')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)

    items = relationship("Item", back_populates="owner")


class School(Base):
    __tablename__ = "school"

    id = Column(String, primary_key=True)
    district = Column(String)
    county = Column(counties_enum)
    name = Column(String)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    osis = Column(String)
    birthdate = Column(Date)
    grade = Column(String)

    # TODO: realtioship school


class Iep(Base):
    __tablename__ = 'iep'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    # TODO: realtioship student


class Mandate(Base):
    __tablename__ = 'mandate'

    id = Column(Integer, primary_key=True)

    service = Column(service_enum)
    group_size = Column(Integer)
    duration = Column(Integer)
    periodicity = Column(periodicity_enum)
    frequency = Column(Integer)
    interval = Column(Integer)

    # TODO: realtioship iep


class Goal(Base):
    __tablename__ = 'goal'

    id = Column(Integer, primary_key=True)

    goal = Column(String)
    criteria = Column(String)
    method = Column(String)
    schedule = Column(String)

    # TODO: relationship iep


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)

    user_role = Column(role_enum)

    # TODO: realtioship user


class Caseload(Base):
    __tablename__ = 'caseload'

    id = Column(Integer, primary_key=True)

    title = Column(String)
    service = Column(service_enum)

    # TODO: user realtiosnhip


class Caseloadee(Base):
    __tablename__ = 'caseloadee'

    id = Column(Integer, primary_key=True)

    # TODO: realtionship caseload
    # TODO: realtionship student
