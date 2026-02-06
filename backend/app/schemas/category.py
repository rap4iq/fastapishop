from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Category name")
    slug: str = Field(..., min_length=3, max_length=50, description="Category slug")


class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Category ID")
    class Config:
        from_attributes = True
