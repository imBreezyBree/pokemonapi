from pydantic import BaseModel, EmailStr, validator



class UserSignInModel(BaseModel):
    email: EmailStr
    password: str

    @validator('password')
    def passwordLength(cls, v):
        if len(v) < 6 and len(v) > 16: 
            raise ValueError('Password must be between 6 and 16 characters')

class UserSignUpModel(UserSignInModel):
    name: str
  

class UserResponseModel(BaseModel):
    name: str
    email: EmailStr
    token: str