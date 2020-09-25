import models
import schemas
from sqlalchemy.orm import Session


def get_user_by_username(db: Session, username: int):
    return db.query(models.User).filter(models.User.username == username).first()


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


def get_all_students(db: Session):
    # REVIEW: look into pagenation and limit fast api docs
    return db.query(models.Student).all()


def get_all_users(db: Session):
    # REVIEW: see above review
    return db.query(models.User).all()


def get_all_cases(db: Session):
    return db.query(models.Case).all()


'''
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
'''
