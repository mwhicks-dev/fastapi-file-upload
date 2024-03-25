from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.sql import Base

class FileModel(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    path: Mapped[str]
