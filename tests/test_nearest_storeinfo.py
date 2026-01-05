from ..tests.base_test import BaseTest
from ..pages.rentomojo_store_experience import RentomojoStoresPage
import pytest
class TestRentomojoStores(BaseTest):
    @pytest.mark.rentomojo
    def test_nearest_rentomojo_stores(self):
        stores=RentomojoStoresPage(self.driver)
        stores.rentomojo_srtores()
