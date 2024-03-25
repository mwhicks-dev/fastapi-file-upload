from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from .sql import Base

class FileModel(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    path: Mapped[str]
