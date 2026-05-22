from fastapi import Depends, APIRouter
from typing import Annotated
from crud.service import BaumService
from crud.router.dependencies import get_service

baum_router = APIRouter(tags=["baum"])

@baum_router.get("")
def get_all(service: Annotated[BaumService, Depends(get_service)]):
    return service.get_all()

@baum_router.get("/{id}")
def get_by_id(id: int, service: Annotated[BaumService, Depends(get_service)]):
    return service.get_by_id(id)
