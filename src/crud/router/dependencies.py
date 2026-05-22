from crud.service.BaumService import BaumService
from crud.repository.BaumRepository import BaumRepository

def get_repository() -> BaumRepository:
    return BaumRepository()

def get_service() -> BaumService:
    return BaumService(get_repository())
