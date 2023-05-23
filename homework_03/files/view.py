from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def SayPong():
    return {"message":"pong"}