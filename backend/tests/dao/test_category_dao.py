import sys
sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from backend.dao.category_dao import CategoryDao
from backend.models.category import Category
import pytest

class TestCategoryDao:
    @pytest.fixture
    def create_instance(self):
        category = Category('Roupas', 'muito bonitas')
        return category

    def test_category_instance(self):
        category_dao = CategoryDao()
        assert isinstance(category_dao, CategoryDao)

    def test_category_save(self, create_instance):
        category_save = CategoryDao().save(create_instance)
        assert category_save.id is not None
        CategoryDao().delete(category_save)

    def test_category_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            category_save = CategoryDao().save('category')

    def test_category_read_by_id(self, create_instance):
        category_save = CategoryDao().save(create_instance)
        category_read = CategoryDao().read_by_id(category_save)
        assert isinstance(category_read, Category)
        CategoryDao().delete(category_read)

    def test_category_read_by_id(self):
        with pytest.raises(TypeError):
            category_read = CategoryDao().read_by_id(category_save)

    def test_category_read_all(self):
        category_read = CategoryDao().read_all()
        assert isinstance(category_read, list)

    def test_category_delete(self, create_instance):
        category_save = CategoryDao().save(create_instance)
        category_read = CategoryDao().read_by_id(category_save)
        CategoryDao().delete(category_read)
        category_read = CategoryDao().read_by_id(category_save)
        assert category_read is None
