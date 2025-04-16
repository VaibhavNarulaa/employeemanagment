from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from usermanagment.model import User
from usermanagment.database import sessionLocal
from usermanagment.auth import SECRET_KEY, ALGORITHM 

#jwt token in autherization header 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db= sessionLocal()
    try:
        yield db 
    finally:
        db.close()


# extract user from token
def get_current_user(token:str=Depends(oauth2_scheme), db:sessionLocal=Depends(get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate credentials")

    try:
        #decode jwt token 
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    #look up the user in the database 
    user=db.query(User).filter(User.username==username).first()
    if user is None: 
        raise credentials_exception 
    
    return user 