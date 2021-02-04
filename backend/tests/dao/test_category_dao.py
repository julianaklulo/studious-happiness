import sys
sys.path.append('.')
import pytest
from backend.dao.category_dao import CategoryDao
from backend.models.category import Category
from sqlalchemy.orm.exc import UnmappedInstanceError

class TestCategoryDao:

    @pytest.fixture
    def create_category(self):
        category = Category('Roupas', 'muito bonitas')
        return category

    def test_category_instance(self):
        category_dao = CategoryDao()
        assert isinstance(category_dao, CategoryDao)

    def test_category_save(self, create_category):
        category_save = CategoryDao().save(create_category)
        assert category_save.id is not None
        CategoryDao().delete(category_save)

    def test_category_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().save('category')

    def test_category_read_by_id(self, create_category):
        category_save = CategoryDao().save(create_category)
        category_read = CategoryDao().read_by_id(category_save.id)
        assert isinstance(category_read, Category)
        CategoryDao().delete(category_read)

    def test_category_read_all(self):
        category_read = CategoryDao().read_all()
        assert isinstance(category_read, list)

    def test_category_delete(self, create_category):
        category_save = CategoryDao().save(create_category)
        category_read = CategoryDao().read_by_id(category_save.id)
        CategoryDao().delete(category_read)
        category_read = CategoryDao().read_by_id(category_read.id)
        assert category_read is None
