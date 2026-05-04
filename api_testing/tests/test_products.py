from api_testing.api_data.api_test_data import StatusCodes, ProductTestData
from api_testing.utils.assertions import assert_status_code

class TestProduct:
    """"Test set for product related verifications."""
    def test_get_products(self, products_api):
        """Test retrieve a single page of products."""
        response = products_api.get_products(page=1)
        assert_status_code(response=response, expected=StatusCodes.OK)
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0

    def test_get_single_product(self, products_api):
        """Test single product retrieval."""
        response = products_api.get_product(product_id=2)
        assert_status_code(response=response, expected=StatusCodes.OK)
        assert response.json()["data"]["id"] == 2
    
    def test_create_product(self, products_api):
        """Test valid product creation."""
        response = products_api.create_product(payload=ProductTestData.valid_product_payload)
        assert_status_code(response=response,expected=StatusCodes.Created)
    
        body = response.json()
        assert body["name"].strip() == "Blue Ribbon"
        assert "id" in body
    
    def test_delete_product(self, products_api):
        """Test product deletion."""
        response = products_api.delete_product(payload=ProductTestData.valid_product_payload)
        assert_status_code(response=response,expected=StatusCodes.Deleted)
    
    def test_create_invalid_product(self, products_api):
        """Test Invalid request to create product."""
        response = products_api.create_product(payload=ProductTestData.invalid_product_payload)
        assert_status_code(response=response, expected=StatusCodes.BadRequest)
        body = response.json()
        assert "error" in body
