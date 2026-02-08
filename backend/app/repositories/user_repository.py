from typing import Optional
from sqlmodel import Session
from app.models import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        super().__init__(session, User)

    def get_by_email(self, email: str) -> Optional[User]:
        from sqlmodel import select
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()