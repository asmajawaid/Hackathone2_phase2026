from abc import ABC
from typing import Generic, TypeVar, List, Optional, Type
from sqlmodel import Session, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType], ABC):
    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    def get_by_id(self, id: str) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.id == id)
        return self.session.exec(statement).first()

    def get_list(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def create(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def update(self, id: str, obj: ModelType) -> Optional[ModelType]:
        existing_obj = self.get_by_id(id)
        if existing_obj:
            # Update fields from the new object
            for key, value in obj.__dict__.items():
                if hasattr(existing_obj, key) and key != '_sa_instance_state':
                    setattr(existing_obj, key, value)
            self.session.add(existing_obj)
            self.session.commit()
            self.session.refresh(existing_obj)
            return existing_obj
        return None

    def delete(self, id: str) -> bool:
        obj = self.get_by_id(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False