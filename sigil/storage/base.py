"""Base classes for storage adapters"""
import abc
from contextlib import asynccontextmanager
from typing import List, Optional

from pydantic import UUID4, BaseModel


class BaseStorage(abc.ABC):
    @abc.abstractmethod
    async def list(self, filter: dict = None) -> List[BaseModel]:
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


class BaseManager:
    _storages = {}

    _storage_classes = {}

    def _init_storage(self, StorageClass):
        return StorageClass()

    def __getattr__(self, name: str):
        if name not in self._storage_classes:
            raise AttributeError(f"no storage called {name}")

        if name not in self._storages or self._storages[name] is None:
            self._storages[name] = self._init_storage(self._storage_classes[name])

        return self._storages[name]

    @classmethod
    @asynccontextmanager
    async def start(cls):
        yield cls()
