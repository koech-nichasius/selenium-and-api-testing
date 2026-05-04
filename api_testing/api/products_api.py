from typing import Any, Dict


class ProductsAPI:
    """This class implements API wrapper for product-related endpoints.
    All operations related to products are encapsulated and HTTP communication delegated
    to the provided API client.
    """
    def __init__(self, client):
        """Initialize the productsAPI."""
        self.client = client

    def get_products(self, page: int = 1) -> Dict[str, Any]:
        """Retrieve a paginated list of products.
        Return response payload or status information from the get action"""
        return self.client.get("/products", params={"page": page})

    def get_product(self, product_id: int) -> Dict[str, Any]:
        """Retrieve a single product by ID.
        Return response payload or status information from the get action"""
        return self.client.get(f"/products/{product_id}")

    def create_product(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new product.
        Return response payload or status information from the post action"""
        return self.client.post("/products", json=payload)

    def delete_product(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Delete a product.
        Return response payload or status information from the delete action"""
        return self.client.delete("/products", json=payload)