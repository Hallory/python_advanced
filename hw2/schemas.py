from pydantic import BaseModel, EmailStr, field_validator

class Address(BaseModel):
    city: str
    street: str
    house_number: int
    
class User(BaseModel):
    name:str
    age:int
    email: EmailStr
    is_employeed: bool
    address: Address
    
    @field_validator("age")
    def check_age_for_employment(cls, age:int ,values:dict):
        is_employeed = values.get("is_employeed")
        
        if is_employeed and not(18 <= age < 65):
            raise ValueError("Age must be between 18 and 65")
        return age
        
    

    