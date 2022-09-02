import pytest
from django.core.management import call_command



@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup,django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata","category_db_fixture")
        call_command("loaddata","category_product_db_fixture")
        call_command("loaddata","product_brand_fixture")
        call_command("loaddata","product_type_fixture")
        call_command("loaddata","product_inventory_db_fixture")
        call_command("loaddata","product_media_db_fixture")
        call_command("loaddata","product_stock_db_fixture")
        call_command("loaddata","product_attribute_fixture")
        call_command("loaddata","product_attribute_value_db_fixture")
        call_command("loaddata","product_attribute_values")
        
        
        
        