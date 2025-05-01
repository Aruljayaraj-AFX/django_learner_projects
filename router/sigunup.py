from fastapi import APIRouter,Depends

router=APIRouter()

@router.post("/signup_verifing")
def signup_verifing(otp_sent=Depends(verifing_user_signup())):
    return{
        "successfully otp sent to email"
    }

