from pydantic import Field, model_validator
from datetime import datetime
from app.schemas.category import CategoryBase
from app.schemas.base_schema import BaseSchema


class QuestionBase(BaseSchema):
    title: str = Field(...,min_length=15, max_length=150)
    description: str | None = Field(default=None, min_length=20, max_length=750)
    start_date: datetime 
    end_date: datetime
    
    category_id: int
    
    @model_validator(mode="after")
    def validate_start_end_date(self):
        if self.start_date > self.end_date:
            raise ValueError("Start date must be before end date")
        return self
        

class QuestionCreateRequest(QuestionBase):
    ...

class QuestionUpdateRequest(BaseSchema):
    title: str | None = Field(default=None, min_length=15, max_length=150)
    description: str | None = Field(default=None, min_length=20, max_length=750)
    start_date: datetime | None = Field(default=None)
    end_date: datetime | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    
    category_id: int | None = None

    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date is not None and self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValueError("Start date must be before end date")
        return self
    

class QuestionRetrieve(BaseSchema):
    id: int
    title: str
    description: str | None
    is_active: bool
    category: CategoryBase | None
    end_date: datetime
    start_date: datetime
    
    
    
    
class QuestionList(BaseSchema):
    id:int
    title: str
    start_date: datetime
    is_active: bool
    category: CategoryBase | None
    
    
class QuestionCreateResponse(QuestionRetrieve):
    ...
    
