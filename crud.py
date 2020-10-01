import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()


def get_caseload(db: Session, caseload_id: int):
    return db.query(models.Caseload).filter(models.Caseload.id == caseload_id).first()


def get_goal(db: Session, goal_id: int):
    return db.query(models.Goal).filter(models.Goal.id == goal_id).first()


def get_mandate(db: Session, mandate_id: int):
    return db.query(models.Mandate).filter(models.Mandate.id == mandate_id).first()


def get_iep(db: Session, iep_id: int):
    return db.query(models.Iep).filter(models.Iep.id == iep_id).first()


def get_school(db: Session, school_id: str):
    return db.query(models.School).filter(models.School.id == school_id).first()


def get_student(db: Session, student_id: id):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_case(db: Session, case_id: id):
    return db.query(models.Case).filter(models.Case.id == case_id).first()


def get_all_students(db: Session):
    # REVIEW: look into pagenation and limit fast api docs
    logging.info(db.query(models.Student).all())
    return db.query(models.Student).all()


def get_all_users(db: Session):
    # REVIEW: see above review
    return db.query(models.User).all()


def get_all_cases(db: Session):
    return db.query(models.Case).all()


def create_user(db: Session, user: schemas.UserCreate):
    not_hasshed = user.password
    db_user = models.User(username=user.username, first_name=user.first_name,
                          last_name=user.last_name, email=user.email, hashed_password=not_hasshed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_role(db: Session, role: schemas.RoleCreate):
    db_role = models.Role(user_role=role.user_role, user_id=role.user_id)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(id=school.id, district=school.district,
                              county=school.county, name=school.name)
    # db_school = models.School(school)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school


def create_student(db: Session, student: schemas.StudentCreate):
    # REVIEW: id string???

    db_student = models.Student(first_name=student.first_name, last_name=student.last_name,
                                osis=student.osis, birthdate=student.birthdate, grade=student.grade, school_id=student.school_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def create_mandate(db: Session, mandate: schemas.MandateCreate):
    db_mandate = models.Mandate(service=mandate.service, group_size=mandate.group_size, duration=mandate.duration,
                                periodicity=mandate.periodicity, frequency=mandate.frequency, interval=mandate.interval, iep_id=mandate.iep_id)
    db.add(db_mandate)
    db.commit()
    db.refresh(db_mandate)
    return db_mandate


def create_iep(db: Session, iep: schemas.IepCreate):
    db_iep = models.Iep(start_date=iep.start_date,
                        end_date=iep.end_date, student_id=iep.student_id)
    db.add(db_iep)
    db.commit()
    db.refresh(db_iep)
    return db_iep


def create_goal(db: Session, goal: schemas.GoalCreate):
    db_goal = models.Goal(goal=goal.goal, criteria=goal.criteria,
                          method=goal.method, schedule=goal.schedule, iep_id=goal.iep_id)

    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal


def create_caseload(db: Session, caseload: schemas.CaseloadCreate):
    db_caseload = models.Caseload(
        title=caseload.title, service=caseload.service, user_id=caseload.user_id)
    db.add(db_caseload)
    db.commit()
    db.refresh(db_caseload)
    return db_caseload


def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.Case(caseload_id=case.caseload_id,
                          student_id=case.student_id)
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


def delete_school(db: Session, school_id: str):
    db_school = get_school(db, school_id)
    if db_school:
        db.delete(db_school)
        db.commit()
        return True
    else:
        return False


def delete_user_by_username(db: Session, username: str):
    db_user = get_user_by_username(db, username)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    else:
        return False


def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    else:
        return False


def delete_mandate(db: Session, mandate_id: int):
    db_mandate = get_mandate(db, mandate_id)
    if db_mandate:
        db.delete(db_mandate)
        db.commit()
        return True
    else:
        return False


def delete_iep(db: Session, iep_id: int):
    db_iep = get_iep(db, iep_id)
    if db_iep:
        db.delete(db_iep)
        db.commit()
        return True
    else:
        return False


def delete_goal(db: Session, goal_id: int):
    db_goal = get_goal(db, goal_id)
    if db_goal:
        db.delete(db_goal)
        db.commit()
        return True
    else:
        return False


def delete_caseload(db: Session, caseload_id: int):
    db_caseload = get_caseload(db, caseload_id)
    if db_caseload:
        db.delete(db_caseload)
        db.commit()
        return True
    else:
        return False


def delete_case(db: Session, case_id: int):
    db_case = get_case(db, case_id)
    if db_case:
        db.delete(db_case)
        db.commit()
        return True
    else:
        return False


def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
        return True
    else:
        return False


def update_object(db: Session, db_object, new_stuff):
    for i in new_stuff:
        setattr(db_object, i[0], i[1])
    db.commit()
    db.refresh(db_object)
    return True


def update_school(db: Session, school_id: int, school: schemas.SchoolCreate):
    db_school = get_school(db, school_id)
    if db_school is None:
        return False
    return update_object(db, db_school, school)


def update_student(db: Session, student_id: int, updated_student: schemas.StudentCreate):
    db_student = get_student(db, student_id)
    if db_student is None:
        return False
    return update_object(db, db_student, updated_student)


def update_mandate(db: Session, mandate_id: int, updated_mandate: schemas.MandateCreate):
    db_mandate = get_mandate(db, mandate_id)
    if db_mandate is None:
        return False
    return update_object(db, db_mandate, updated_mandate)


def update_iep(db: Session, iep_id: int, updated_iep: schemas.MandateCreate):
    db_iep = get_iep(db, iep_id)
    if db_iep is None:
        return False
    return update_object(db, db_iep, updated_iep)


def update_goal(db: Session, goal_id: int, updated_goal: schemas.GoalCreate):
    db_goal = get_goal(db, goal_id)
    if db_goal is None:
        return False
    return update_object(db, db_goal, updated_goal)


def update_caseload(db: Session, caseload_id: int, updated_caseload: schemas.CaseloadCreate):
    db_caseload = get_caseload(db, caseload_id)
    if db_caseload is None:
        return False
    return update_object(db, db_caseload, updated_caseload)


def update_role(db: Session, role_id: int, updated_role: schemas.RoleCreate):
    db_role = get_role(db, role_id)
    if db_role is None:
        return False

    return update_object(db, db_role, updated_role)
