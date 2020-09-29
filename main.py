import logging
from typing import List

import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

logging.basicConfig(filename='main.log',
                    format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logging.warning("New Run Starts Here")

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{username}", response_model=schemas.User)
def read_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/role/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@app.get("/caseload/{caseload_id}", response_model=schemas.Caseload)
def read_caseload(caseload_id: int, db: Session = Depends(get_db)):
    caseload = crud.get_caseload(db, caseload_id=caseload_id)
    if caseload is None:
        raise HTTPException(status_code=404, detail="Caseload not found")
    return caseload


@app.get("/goal/{goal_id}", response_model=schemas.Goal)
def read_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = crud.get_goal(db, goal_id=goal_id)
    if goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal


@app.get("/mandate/{mandate_id}", response_model=schemas.Mandate)
def read_mandate(mandate_id: int, db: Session = Depends(get_db)):
    mandate = crud.get_mandate(db, mandate_id=mandate_id)
    if mandate is None:
        raise HTTPException(status_code=404, detail="Mandate not found")
    return mandate


@app.get("/iep/{iep_id}", response_model=schemas.Iep)
def read_iep(iep_id: int, db: Session = Depends(get_db)):
    iep = crud.get_iep(db, iep_id=iep_id)
    if iep is None:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep


@app.get("/school/{school_id}", response_model=schemas.School)
def read_school(school_id: str, db: Session = Depends(get_db)):
    school = crud.get_school(db, school_id=school_id)
    if school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@app.get("/student/{student_id}", response_model=schemas.Student)
def read_student(student_id: int,  db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/students", response_model=List[schemas.Student])
def read_all_students(db: Session = Depends(get_db)):
    students = crud.get_all_students(db)
    if not students:
        raise HTTPException(status_code=404, detail="Students not found")
    return students


@app.get("/users", response_model=List[schemas.User])
def read_all_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    print(users)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@app.get("/case/{case_id}", response_model=schemas.Case)
def read_case(case_id: int, db: Session = Depends(get_db)):
    case = crud.get_case(db, case_id=case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@app.get("/cases", response_model=List[schemas.Case])
def read_all_cases(db: Session = Depends(get_db)):
    cases = crud.get_all_cases(db)
    if not cases:
        raise HTTPException(status_code=404, detail="cases not found")
    return cases


@app.get("/cases/byUserId/{user_id}", response_model=schemas.User)
def read_cases_by_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.cases


@app.post("/user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/role")
def create_role_user(role: schemas.RoleCreate, user_id: int, db: Session = Depends(get_db)):
    role.user_id = user_id
    return crud.create_role(db=db, role=role)


@app.post("/school")
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return crud.create_school(db=db, school=school)


@app.post("/student")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@app.post("/mandate")
def create_mandate(mandate: schemas.MandateCreate, db: Session = Depends(get_db)):
    return crud.create_mandate(db=db, mandate=mandate)


@app.post("/iep")
def create_iep(iep: schemas.IepCreate, db: Session = Depends(get_db)):
    return crud.create_iep(db=db, iep=iep)


@app.post("/goal")
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db)):
    return crud.create_goal(db=db, goal=goal)


@app.post("/caseload")
def create_caseload(caseload: schemas.CaseloadCreate, db: Session = Depends(get_db)):
    return crud.create_caseload(db=db, caseload=caseload)


@app.post("/case")
def create_case(case: schemas.CaseCreate, db: Session = Depends(get_db)):
    return crud.create_case(db=db, case=case)


@app.post("/role")
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db=db, role=role)


@app.delete("/user/{username}")
def delete_user(username: str, db: Session = Depends(get_db)):
    deleted = crud.delete_user_by_username(db=db, username=usernames)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Username not found")
    return username


@app.delete("/school/{school_id}")
def delete_school(school_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_school(db=db, school_id=school_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="School not found")
    return school_id


@app.delete("/student/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db=db, student_id=student_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_id


@app.delete("/mandate/{mandate_id}")
def delete_mandate(mandate_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_mandate(db=db, mandate_id=mandate_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Mandate not found")
    return mandate_id


@app.delete("/iep/{iep_id}")
def delete_iep(iep_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_iep(db=db, iep_id=iep_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep_id


@app.delete("/goal/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_goal(db=db, goal_id=goal_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal_id


@app.delete("/caseload/{caseload_id}")
def delete_caseload(caseload_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_caseload(db=db, caseload_id=caseload_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Caseload not found")
    return caseload_id


@app.delete("/case/{case_id}")
def delete_case(case_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_case(db=db, case_id=case_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Case not found")
    return case_id


@app.delete("/role/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_role(db=db, role_id=role_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_id


@app.put("/user/{username}")
def update_user(username: str, db: Session = Depends(get_db)):
    # TODO: finish this
    pass


@app.put("/school/{school_id}")
def update_school(school: schemas.SchoolCreate, school_id: str, db: Session = Depends(get_db)):
    updated = crud.update_school(db=db, school_id=school_id, school=school)
    if updated is False:
        raise HTTPException(status_code=404, detail="School not found")
    return school.id


@app.put("/student/{student_id}")
def update_student(updated_student: schemas.StudentCreate, student_id: int, db: Session = Depends(get_db)):
    updated = crud.update_student(
        db=db, student_id=student_id, updated_student=updated_student)
    if updated is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_id


@app.put("/mandate/{mandate_id}")
def update_mandate(updated_mandate: schemas.MandateCreate, mandate_id: int, db: Session = Depends(get_db)):
    updated = crud.update_mandate(
        db=db, mandate_id=mandate_id, updated_mandate=updated_mandate)
    if updated is False:
        raise HTTPException(status_code=404, detail="Mandate not found")
    return mandate_id


@app.put("/iep/{iep_id}")
def update_iep(updated_iep: schemas.IepCreate, iep_id: int, db: Session = Depends(get_db)):
    updated = crud.update_iep(db=db, iep_id=iep_id, updated_iep=updated_iep)
    if update is False:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep_id


@app.put("/goal/{goal_id}")
def update_goal(updated_goal: schemas.GoalCreate, goal_id: int, db: Session = Depends(get_db)):
    updated = crud.update_goal(
        db=db, goal_id=goal_id, updated_goal=updated_goal)
    if update is False:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal_id


@app.put("/caseload/{caseload_id}")
def update_caseload(updated_caseload: schemas.CaseloadCreate, caseload_id: int, db: Session = Depends(get_db)):
    updated = crud.update_caseload(
        db=db, caseload_id=caseload_id, updated_caseload=updated_caseload)
    if update is False:
        raise HTTPException(status_code=404, detail="caseload not found")
    return caseload_id


@app.put("/case/{case_id}")
def updated_case(updated_case: schemas.CaseCreate, case_id: int, db: Session = Depends(get_db)):
    updated = crud.update_case(
        db=db, case_id=case_id, updated_case=updated_case)
    if update is False:
        raise HTTPException(status_code=404, detail="case not found")
    return case_id


@app.put("/role/{role_id}")
def update_role(updated_role: schemas.RoleCreate, role_id: int, db: Session = Depends(get_db)):
    updated = crud.update_role(
        db=db, role_id=role_id, updated_role=updated_role)
    if updated is False:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_id
