from pydantic import BaseModel, EmailStr


class UserCreateResponse(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str


class UserResponse(BaseModel):
    name: str
    email: EmailStr
    password: str

    model_config = {
        "from_attributes": True,
    }
