import sys
sys.path.append('.')
import pytest
from backend.controller.base_controller import BaseController
from backend.controller.category_controller import CategoryController
from backend.models.category import Category

class TestCategoryController:

    @pytest.fixture
    def create_instance(self):
        category = CategoryController()
        return category

    def test_category_controller_instance(self, create_instance):
        assert isinstance(create_instance, CategoryController)

    def test_category_create(self, create_instance):
        pass


    def test_read_all_return_list(create_instance):
        result = create_instance.read_all()
        assert isinstance(result, list)

    def test_category_read_by_id():
        controller = CategoryController()
        with pytest.raises(Exception) as exc:
            controller.read_by_id(1234)
        assert str(exc.value) == 'Object not found in the database.'