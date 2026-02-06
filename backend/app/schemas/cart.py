from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Product quantity")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(CartItemBase):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Product quantity")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Product quantity")
    subtotal: float = Field(..., description="Subtotal price")
    image_url: str = Field(..., description="Product image URL")



class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="Cart items")
    total: float = Field(..., description="Total price")
    items_count: int = Field(..., description="Total number of items")
    