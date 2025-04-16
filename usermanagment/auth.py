from passlib.context import CryptContext
from datetime import datetime , timedelta
from jose import JWTError , jwt 

#secret key 
SECRET_KEY="QWERTY"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#PASSWORD HASHING 
pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")

#fuction to hash password before saving 
def hash_password(password:str):
    return pwd_context.hash(password)

#function to check if pain password matched the hash password 
def verify_password(plain, hashed):
    return pwd_context.verify(plain , hashed)

#fucntion to create jwt token 
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
