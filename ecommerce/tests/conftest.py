from pytest_factoryboy import register

from ecommerce.tests.factories import BrandFactory, CategoryFactory, ProductFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
