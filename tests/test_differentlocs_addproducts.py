from ..pages.rentomojo_location_handling import LocationHandling
from ..tests.base_test import BaseTest
import pytest
class TestAddProducts(BaseTest):


    @pytest.mark.rentomojo

    def test_addDifferentLocationsProducts(self):
        lochandle=LocationHandling(self.driver)
        lochandle.add_products_different_locations()