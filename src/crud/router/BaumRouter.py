from typing import Final
from fastapi import Request
from urllib import request
from typing import Any
from ast import Dict
from crud.router.BaumModel import BaumModel
from crud.router.dependencies import get_service
from fastapi import Depends, APIRouter
from typing import Annotated
from crud.service import BaumService
from loguru import logger


baum_router = APIRouter(tags=["baum"])

@baum_router.get("/all", status_code=200)
def get_all(service: Annotated[BaumService, Depends(get_service)]):
    logger.info("Get all baeume")
    return service.get_all()

@baum_router.get("/{id}", status_code=200)
def get_by_id(id: int, service: Annotated[BaumService, Depends(get_service)]):
    logger.info(f"Get baum by id: {id}")
    return service.get_by_id(id)

@baum_router.post("", status_code=201)
def add(baum: BaumModel, service: Annotated[BaumService, Depends(get_service)]) -> int:
    logger.info(f"Add baum: {baum}")
    return service.add(baum.to_entity())

@baum_router.put("/{id}", status_code=204)
def update(id: int, baum: BaumModel, service: Annotated[BaumService, Depends(get_service)]) -> None:
    logger.info(f"Update baum: {baum}")
    service.update_by_id(id, baum.to_entity())

@baum_router.delete("/{id}", status_code=204)
def delete(id: int, service: Annotated[BaumService, Depends(get_service)]) -> None:
    logger.info(f"Delete baum by id: {id}")
    service.delete_by_id(id)

@baum_router.get("", status_code=200)
def get(request: Request, service: Annotated[BaumService, Depends(get_service)]):
    query: Final = request.query_params
    logger.info(f"Get baeume with query: {query}")
    params = dict(query)
    return service.get(params)


