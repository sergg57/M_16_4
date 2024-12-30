# -*- coding: utf-8 -*-
from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: str

@app.get("/users")
async def get_all_users()-> List[User]:
    return users

@app.post("/user/{username}/{age}")
def create_user(username: str, age: str):
    user = User(id=len(users)+1, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: str):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User wos not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User wos not found")