import sys
sys.path.append('.')
import pytest
from backend.controller.base_controller import BaseController
from backend.controller.category_controller import CategoryController
from backend.models.category import Category

@pytest.fixture
def create_instance():
    category = CategoryController()
    return category

def test_category_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CategoryController)

def test_create_category(create_instance):
    name = 'Category'
    description = 'Test'
    category = Category(name, description)
    result = create_instance.save(category)
    assert result.id is not None
    assert result.name == name
    assert result.description == description
    create_instance.delete(result)


def test_update_category(create_instance):
    name = 'Category'
    description = 'Test'
    category = Category(name, description)
    created = create_instance.save(category)
    created.name = 'Category 2'
    created.description = 'Test 2'
    result = create_instance.update(created)
    assert result.id is not None
    assert result.name == 'Category 2'
    assert result.description == 'Test 2'
    create_instance.delete(result)


def test_delete_category(create_instance):
    name = 'Category'
    description = 'Test'
    category = Category(name, description)
    created = create_instance.save(category)
    create_instance.delete(created)
    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(created.id)
        assert exc.value == 'Object not found in the database.'


def test_read_by_id_should_return_category(create_instance):
    name = 'Category'
    description = 'Test'
    category = Category(name, description)
    created = create_instance.save(category)
    result = create_instance.read_by_id(created.id)
    assert isinstance(result, Category)
    assert result.name == name
    assert result.description == description
    create_instance.delete(created)
