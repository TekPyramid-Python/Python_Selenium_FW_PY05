from ..tests.base_test import BaseTest
from ..pages.rentomojo_homepage import RentomojoHomepage
import pytest

class TestHomepage(BaseTest):
    @pytest.mark.rentomojo
    def test_homepage(self):
        homepage = RentomojoHomepage(self.driver)
        homepage.addingproduct_tocart()