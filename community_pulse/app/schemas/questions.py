from pydantic import BaseModel, Field, model_validator, ConfigDict
from datetime import datetime

class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid"
        
    )
    
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
    
    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date is not None and self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValueError("Start date must be before end date")
        return self
    

class QuestionRetrieve(QuestionBase):
    id: int
    is_active: bool
    
    
class QuestionList(BaseSchema):
    id:int
    title: str
    start_date: datetime
    is_active: bool
    
    
class QuestionCreateResponse(QuestionRetrieve):
    ...
    
