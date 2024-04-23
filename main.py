from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers.user import router as UserRouter
from os import environ
from dotenv import load_dotenv


app = FastAPI()


@app.get("/")
async def test():
    return {"message": "covid-19 api"}


app.include_router(UserRouter,tags=["User"],prefix="/user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)