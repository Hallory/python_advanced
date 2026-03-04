from pydantic import BaseModel, Field
from app.schemas.questions import QuestionList

class CategoryBase(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=100)
    
class CategoryCreateRequest(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    
class CategoryResponse(CategoryBase):
    pass
