from pydantic import Field
from app.schemas.base_schema import BaseSchema

class CategoryBase(BaseSchema):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=100)


class CategoryCreateRequest(BaseSchema):
    name: str = Field(min_length=3, max_length=100)


class CategoryUpdateRequest(BaseSchema):
    name: str = Field(min_length=3, max_length=100)


class CategoryResponse(CategoryBase):
    ...