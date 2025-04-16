from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from usermanagment import model , schemas ,utils 

router = APIRouter()

#manager only routes to get all user 
@router.get("/manager-dashboard", response_model=list[schemas.UserOut])
def get_all_user(
    currernt_user:model.User=Depends(utils.get_current_user),
    db : Session = Depends(utils.get_db)
    ):
    if not currernt_user.is_manager:
        raise HTTPException(status_code=403 , detail="ACCESS DENIED : MANAGER ONLY ")
    
    users=db.query(model.User).all()
    return users