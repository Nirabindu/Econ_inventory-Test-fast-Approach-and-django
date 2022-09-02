import pytest
from ecommerce_inventory.core import models
from django.db import IntegrityError


# this approach we are using fixture.json file to check out the data
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name,slug,is_active",
    [
        (1,"fashion","fashion",1),
        (18,"trainers","trainers",1),
        (35,"baseball","baseball",1),
    ]
)
def test_category_dbfixture(
    db,db_fixture_setup,id,name,slug,is_active
):
    # this data coming from fixture.json via test database
    result = models.Category.objects.get(id = id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active ==  is_active



# using factory boy
# in factory we need not to use fixture.json

@pytest.mark.parametrize(
    "name,slug,is_active",
    [
        ("fashion","fashion",1),
        ("trainers","trainers",1),
        ("baseball","baseball",1),
    ]
)
def test_category_data(
    db,category_factory,name,slug,is_active
):
    # if we not passing any field like name that will created ny faker randomly that we have create our factories
    # i.e it will replace the factories data to parameterize data 
    result = category_factory.create(name=name, slug = slug,  is_active= is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active ==  is_active
    
    
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id ,web_id,name,slug,description,is_active,created_at,updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        )
    ],
)
def test_product_db_fixture(db,db_fixture_setup,id ,web_id,name,slug,description,is_active,created_at,updated_at):
    result = models.Product.objects.get(id=id)
    
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    
    
    assert result.name == name
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at    
    
# web_id of product table uniqeness check 
def test_product_db_uniqueness_integrity(db,product_factory):
    new_web_id = product_factory.create(web_id = 123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id = 123456789)
 
  
pytest.mark.dbfixture        
def test_product_db_insert_data(
    db,product_factory,db_fixture_setup
):
    # new_category = category_factory.create()
    new_product = product_factory.create(category = (1,2,35))
    # the category id is getting from category fixture
    # the table should be like product_id category_id
    # 1,1 and 1,2, 1,52 like that
    result = new_product.category.all().count()
  
    
    assert "web_id_" in new_product.web_id  
    assert result == 3



# Inventory model
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku,upc,product_type,product,brand,is_active,retail_price,store_price,sale_price,weight,created_at,updated_at",
    [
        (
            1,
            "7633969397",
            "934093051374",
            1,
            1,
            1,
            1,
            97.00,
            92.00,
            46.00,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
            (
            8616,
            "3880741573",
            "844935525855",
            1,
            8616,
            1253,
            1,
            89.00,
            84.00,
            42.00,
            929,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ]
)
def test_inventory_db_fixtures(
    db,db_fixture_setup,id, sku,upc,product_type,product,brand,is_active,retail_price,store_price,sale_price,weight,created_at,updated_at
):
    
    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product 
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at
    
    
# inserting data to inventory
def test_inventory_db_product_insert(
    db,product_inventory_factory,
):
    new_prod = product_inventory_factory.create(
        
        sku = "123456789",
        upc = "123456789",
        product_type__name = "new_name",
        product__web_id = "123456789",
        brand__name="new_name",
    )

    assert new_prod.sku == "123456789"
    assert new_prod.upc == "123456789"
    assert new_prod.product_type.name == "new_name"
    
# inventory sku and upc unique integrity check
def test_product_inventory_uniqueness_check(db,product_inventory_factory):
    #     new_web_id = product_factory.create(web_id = 123456789)
#     with pytest.raises(IntegrityError):
#         product_factory.create(web_id = 123456789)

    new_sku = product_inventory_factory.create(sku="12345678",upc="1234" )
    with pytest.raises(IntegrityError):
        product_inventory_factory.create(sku = "12345678",upc="1234")
    


# product type model test
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name",
    [
        (1,"shoes")
    ]
)
def test_product_type_model_test(db,db_fixture_setup,id,name):
    result = models.ProductType.objects.get(id=id)
    assert result.name == "shoes"
    
def test_product_type_insertdata(db,product_type_factory):
    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"

def test_product_type_uniqueness(db,product_type_factory):
    product_type_factory.create(name="new_name")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="new_name")



@pytest.mark.dbfixture  
@pytest.mark.parametrize(
    "id, name",
    [
        (1,"361"),
        (2,"143 girl"),
        (4,"2 lips too"),
        (6,"9 degree by refex"),
    ]
)     
def test_brand(db,db_fixture_setup,id,name):
    result = models.Brand.objects.get(id=id)
    
    assert result.name == name
    
def test_brand_insert(db,brand_factory):
    new_type = brand_factory.create(name="new_name")
    assert new_type.name == "new_name"
    
def test_brand_unique_test(db,brand_factory):
    new_brand = brand_factory.create(name="new_brand")
    with pytest.raises(IntegrityError):
        new_brand = brand_factory.create(name="new_brand")

# test inventory db_media

@pytest.mark.dbfixture  
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            1,
            1,
            "images/default.png",
            "a default image solid color",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            8616,
            "images/default.png",
            "a default image solid color",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_media_dataset(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    image,
    alt_text,
    is_feature,
    created_at,
    updated_at,
):
    result = models.Media.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    
    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text


# test_product_media_insert
def test_product_media_insert(db,media_factory):
    new_media = media_factory.create(product_inventory__sku ="12345678")
    assert new_media.product_inventory.sku == "12345678"
    assert new_media.image == "images/default.png"
    assert new_media.alt_text == "a default image solid color"
    assert new_media.is_feature == 1
    


# test Stock table

@pytest.mark.dbfixture  
@pytest.mark.parametrize(
    "id, product_inventory, last_checked, units, units_sold",
    [
        (1, 1, "2021-09-04 22:14:18", 135, 0),
        (8616, 8616, "2021-09-04 22:14:18", 100, 0)
    ],
)
def test_inventory_db_stock_dataset(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    last_checked,
    units,
    units_sold,
):
    result = models.Stock.objects.get(id=id)
    
    result_last_checked = result.last_checked.strftime("%Y-%m-%d %H:%M:%S")
    assert result.product_inventory.id == product_inventory
    assert result_last_checked == last_checked
    assert result.units == units
    assert result.units_sold == units_sold

# test stock table data insert
def test_stock_product_insert(db,stock_factory):
    new_stock = stock_factory.create(product_inventory__sku ="123456")
    assert new_stock.product_inventory.sku == "123456"
    assert new_stock.last_checked == "2021-09-04 22:14:18"
    assert new_stock.units == 135
    assert new_stock.units_sold == 0
    
    
# test product Attribute

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, description",
    [
        (1, "men-shoe-size", "men shoe size"),
    ],
)
def test_inventory__product_attribute(db,db_fixture_setup, id, name, description):
    new_attribute = models.ProductAttribute.objects.get(id = id)
    assert new_attribute.name == "men-shoe-size"
    assert new_attribute.description == "men shoe size"
    
def test_inventory_product_attribute_data_insert(db,product_attribute_factory):
    
    new_product_attribute = product_attribute_factory.create()
    assert new_product_attribute.name == "men-shoe-size-0"
    assert new_product_attribute.description == "men shoe size0"

# product attribute values

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_attribute, attribute_value",
    [
        (1, 1, 10),
    ],
)
def test_product_attribute_value(db,db_fixture_setup,id,product_attribute, attribute_value):
    result = models.ProductAttributeValue.objects.get(id = id)
    assert result.product_attribute.id == 1
    assert result.attribute_value == "10"
    


# create to database
def test_inventory_db_product_attribute_value_data(
    db, product_attribute_value_factory
):
    new_attribute_value = product_attribute_value_factory.create(
        attribute_value="new_value", product_attribute__name="new_value"
    )
    assert new_attribute_value.attribute_value == "new_value"
    assert new_attribute_value.product_attribute.name == "new_value"
 
 
 
    
# def test_inventory_db_insert_inventory_product_values(
#     db, product_with_attribute_values_factory
# ):

#     new_inv_attribute = product_with_attribute_values_factory(sku="123456789")
#     result = models.ProductInventory.objects.get(sku="123456789")
#     count = result.attribute_values.all().count()
#     assert count == 2