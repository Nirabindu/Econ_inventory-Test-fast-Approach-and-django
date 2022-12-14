import pytest
import factory
from faker import Faker
from pytest_factoryboy import register
from ecommerce_inventory.core import models

fake = Faker()



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
    # creating data
    # for creating random data uniquely
    # nae = factory.sequence(lambda n:"cat_slug_%d" %n)
    name = fake.lexify(text = "cat_name_??????")
    slug = fake.lexify(text = "cat_slug_??????")
    
        
class productFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product
    
    web_id  = factory.sequence(lambda n:"web_id_%d" %n)
    slug = fake.slug()
    name = fake.name()
    description = fake.text()
    #  category = factory.SubFactory(CategoryFactory)
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"
    
    @factory.post_generation
    def category(self,create, extracted, **kwargs):
        if not create or not extracted:
            return 
        if extracted:
            for cat in extracted:
                self.category.add(cat)
 
 
       
class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType

    name = factory.Sequence(lambda n: "type_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda n: "brand_%d" % n)


        
class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = factory.Sequence(lambda n: "sku_%d" % n)
    upc = factory.Sequence(lambda n: "upc_%d" % n)
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(productFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = 1
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987    
    



class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType
        
    name = factory.sequence(lambda n: "name_%d" %n)
    

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand
    name = factory.sequence(lambda n: "name_%d" %n)




class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Media
    product_inventory = factory.SubFactory(ProductInventoryFactory)
    image = "images/default.png"
    alt_text ="a default image solid color"
    is_feature = True
        

class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Stock
    product_inventory = factory.SubFactory(ProductInventoryFactory)
    last_checked = "2021-09-04 22:14:18"
    units = 135
    units_sold = 0
    

class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttribute
    
    name = "men-shoe-size-0"
    description = "men shoe size0"
    


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = fake.lexify(text="attribute_value_??????")





# class ProductAttributeValuesFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.ProductAttributeValues

#     attributevalues = factory.SubFactory(ProductAttributeValueFactory)
#     productinventory = factory.SubFactory(ProductInventoryFactory)


# class ProductWithAttributeValuesFactory(ProductInventoryFactory):
#     attributevalues1 = factory.RelatedFactory(
#         ProductAttributeValuesFactory,
#         factory_related_name="productinventory",
#     )
#     attributevalues2 = factory.RelatedFactory(
#         ProductAttributeValuesFactory,
#         factory_related_name="productinventory",
#     )












    

register(CategoryFactory)
register(productFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
register(MediaFactory)
register(StockFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
# register(ProductAttributeValuesFactory)
