"""Base classes for store adapters"""
import abc
from typing import List, Optional

from pydantic import UUID4, BaseModel


class BaseStore(abc.ABC):
    @abc.abstractmethod
    async def list(self) -> List[BaseModel]:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, uuid: UUID4) -> Optional[BaseModel]:
        raise NotImplementedError

    @abc.abstractmethod
    async def save(self, entity: BaseModel):
        raise NotImplementedError

    @abc.abstractmethod
    async def save_all(self, entities: List[BaseModel]):
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, uuid: UUID4):
        raise NotImplementedError
