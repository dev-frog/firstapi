from fastapi import APIRouter, Depends
from pycaret.datasets import get_data
from pycaret.regression import *

from model.user import UserModel

router = APIRouter()

@router.post("/")
async def user(data: UserModel):
    # create a user
    return {"message": "User created", "data": data}


@router.get("/")
async def user():
    # get all users
    return {"message": "Get all users"}

@router.get("/{user_id}")
async def user(user_id: int):
    # get a user by id
    return {"message": f"Get user with id {user_id}"}

@router.put("/{user_id}")
async def user(user_id: int):
    # update a user by id
    return {"message": f"Update user with id {user_id}"}

@router.delete("/{user_id}")
async def user(user_id: int):
    # delete a user by id
    return {"message": f"Delete user with id {user_id}"}

