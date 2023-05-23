import uvicorn
from fastapi import FastAPI
from view import router as rs

app = FastAPI()
app.include_router(rs)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True,)
