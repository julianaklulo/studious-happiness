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

    @pytest.fixture
    def create_category(self):
        category = Category('name', 'description')
        return category

    def test_category_controller_instance(self, create_instance):
        assert isinstance(create_instance, CategoryController)

    def test_read_all_return_list(self, create_instance):
        result = create_instance.read_all()
        assert isinstance(result, list)

    def test_category_create(self, create_instance, create_category):
        category = create_instance.save(create_category)
        assert category.id is not None
        create_instance.delete(category)

    def test_category_read_by_id(self, create_instance, create_category):
        category = create_instance.save(create_category)
        category_read = create_instance.read_by_id(category.id)
        assert isinstance(category_read, Category)
        create_instance.delete(category_read)

    def test_category_delete(self, create_instance, create_category):
        category = create_instance.save(create_category)
        create_instance = CategoryController()
        with pytest.raises(Exception) as exc:
            create_instance.read_by_id(category.id)
        assert exc.value == 'Object not found in the database.'