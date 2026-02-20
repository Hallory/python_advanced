from pydantic import BaseModel, Field

class Category(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=100)
    
class CategoryCreateRequest(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    
class CategoryResponse(Category):
    pass