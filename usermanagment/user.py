from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm  import Session
from fastapi.security import OAuth2PasswordRequestForm
from usermanagment import schemas,model,auth,utils

router = APIRouter()
 
#register a new user 

@router.post("/register", response_model=schemas.UserOut)
def register_user(user:schemas.UserCreate , db: Session = Depends(utils.get_db)):
    existing_user=db.query(model.User).filter(model.User.username==user.username).first()
    if existing_user:
        raise HTTPException(status_code=400 , detail="Username already registered ")
    
    hashed_password=auth.hash_password(user.password)
    new_user=model.User(username=user.username,email=user.email , password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#login user 
@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(utils.get_db)):
    user=db.query(model.User).filter(model.User.username==form_data.username).first()
    if not user or not auth.verify_password(form_data.password,user.password):
        raise HTTPException(status_code=400 , detail="Invali credentials ")
    
    token = auth.create_access_token(data={"sub":user.username})
    return {"access token ": token , "token_type ": "bearer"}

#user dashboard 
@router.get("/dashboard", response_model=schemas.UserOut)
def user_dashboard(current_user : model.User =Depends(utils.get_current_user)):
    return current_user