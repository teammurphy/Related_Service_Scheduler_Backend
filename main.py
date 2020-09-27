from typing import List

import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

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


@ app.get("/cases", response_model=List[schemas.Case])
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


@app.post("/users/{user_id}/role/")
def create_role(role: schemas.RoleCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_role(db=db, role=role, user_id=user_id)


'''

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

'''
