import sys

sys.path.append('.')
from backend.models.category import Category
import pytest


class TestCategory:
    name = "Category"
    description = "A very nice category"

    @pytest.mark.parametrize("name, description",
                                [('N', ''), ('N'*100, 'D'*255)]
                            )
    def test_create_instance(self, name, description):
        category = Category(name, description)
        assert isinstance(category, Category)

    @pytest.mark.parametrize("name", ['', ' ', 'N' * 101])
    def test_category_name_not_value(self, name):
        with pytest.raises(ValueError):
            category = Category(name, self.description)


    @pytest.mark.parametrize("name", [None, True, 123, 123.4])
    def test_category_name_not_type(self, name):
        with pytest.raises(TypeError):
            category = Category(name, self.description)


    @pytest.mark.parametrize("description", ['N'*256])
    def test_category_description_not_value(self, description):
        with pytest.raises(ValueError):
            category = Category(self.name, description)
