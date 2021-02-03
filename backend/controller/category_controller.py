import sys
sys.path.append('.')
from backend.controller.base_controller import BaseController
from backend.dao.category_dao import CategoryDao

class CategoryController(BaseController):
    def __init__(self):
        super().__init__(CategoryDao)


c = CategoryDao().read_by_id(1)
print(c)