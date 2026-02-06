from sqlalchemy.orm import Session
from typing import List
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository
from app.schemas.product import ProductResponse, ProductCreate, ProductListResponse
from fastapi import HTTPException, status

class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all_products(self) -> List[ProductResponse]:
        products = self.product_repository.get_all()
        product_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=product_response, total=len(product_response))

    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return ProductResponse.model_validate(product)

    def get_product_by_category(self, category_id: int) -> ProductListResponse:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

        products = self.product_repository.get_by_category_id(category_id)
        product_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=product_response, total=len(product_response))

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        category = self.category_repository.get_by_id(product_data.category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        product = self.repository.create(product_data)
        return ProductResponse.model_validate(product)

