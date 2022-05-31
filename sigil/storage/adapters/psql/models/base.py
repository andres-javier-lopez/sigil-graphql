from __future__ import annotations

from abc import abstractmethod

from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy.orm.decl_api import declarative_base

Base = declarative_base()


class EntityModel:
    db_fields = set()

    @classmethod
    def from_entity(cls, entity: PydanticBaseModel) -> EntityModel:
        fields = entity.dict(include=cls.db_fields)
        for field in cls.db_fields:
            if field not in fields:
                fields[field] = getattr(entity, field)
        return cls(**fields)

    def set_entity(self, entity: PydanticBaseModel):
        for field in self.db_fields:
            if field == "uuid":
                continue
            setattr(self, field, getattr(entity, field))

    @abstractmethod
    def get_entity(self) -> PydanticBaseModel:
        raise NotImplementedError
