import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from ecommerce.tests.factories import BrandFactory, CategoryFactory, ProductFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)


@pytest.fixture
def api_client():
    return APIClient
