from uuid import UUID

from pydantic import BaseModel

class FileModel(BaseModel):
    id: UUID
