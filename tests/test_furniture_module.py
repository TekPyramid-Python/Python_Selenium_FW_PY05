from ..tests.base_test import BaseTest
from ..pages.furniture_page import Furniture_Module
import pytest

class TestFurnitureProductFlow(BaseTest):
    @pytest.mark.rentomojo

    def test_add_furniture_product(self):
        furniture=Furniture_Module(self.driver)
        furniture.adding_furniture_product()

