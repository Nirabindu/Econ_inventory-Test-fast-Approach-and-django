# this file always running before run any test
# ex loading diff fixtures etc and this file should be in root directory


# before test run all the tests run the selenium file should run first
pytest_plugins = [
    "ecommerce_inventory.test.fixtures",
    "ecommerce_inventory.test.factories",

]