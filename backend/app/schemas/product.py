from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Product price")
    image_url: Optional[str] = Field(None, description="Product image URL")
    category_id: int = Field(..., description="Product category ID")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(..., description="Product ID")
    name: str
    description: str
    price: float
    image_url: str
    created_at: datetime
    category_id: int
    category: CategoryResponse = Field(..., description="Product category")
    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products")
    