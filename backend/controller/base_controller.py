from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel

class BaseController:
    def __init__(self, dao: BaseDao):
        self.__dao = dao

    def save(self, model: BaseModel) -> None:
        return self.__dao.save(model)

    def read_by_id(self, id: int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        return result

    def read_all(self) -> list:
        result = self.__dao.read_all()
        return result

    def update(self, model: BaseModel) -> None:
        self.__dao.save(model)

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
