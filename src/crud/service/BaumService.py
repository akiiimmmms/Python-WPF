
from ast import Dict
from crud.service.NotFoundException import NotFoundException
from crud.repository.BaumRepository import BaumRepository
from crud.entity.Baum import Baum
from loguru import logger

class BaumService:
    def __init__(self, baum_repository: BaumRepository):
        self.baum_repository = baum_repository

    def add(self, baum: Baum) -> int:
        logger.info(f"Add baum: {baum}")
        return self.baum_repository.add(baum)

    def get_by_id(self, id: int) -> Baum | None:
        logger.info(f"Get baum by id: {id}")
        baum = self.baum_repository.get(id)
        if baum is None:
            raise NotFoundException(id)
        return baum

    def update_by_id(self, id: int, baum: Baum) -> None:
        logger.info(f"Update baum by id: {id}")
        existing_baum = self.baum_repository.get(id)
        if existing_baum is None:
            raise NotFoundException(id)
        baum.set(id=id)
        self.baum_repository.update(baum)

    def delete_by_id(self, id: int) -> None:
        logger.info(f"Delete baum by id: {id}")
        baum = self.baum_repository.get(id)
        if baum is None:
            raise NotFoundException(id)
        self.baum_repository.delete(id)

    def get_all(self) -> list[Baum]:
        logger.info("Get all baeume")
        return self.baum_repository.get_all()
    
    def get(self, query: Dict[str, str]) -> list[Baum]:
        logger.info(f"Get baeume with query: {query}")
        if query.keys() == "":
            return self.get_all()
        baeume = self.baum_repository.get_with_query(query)
        if baeume is None:
            raise NotFoundException(query)
        return baeume
    