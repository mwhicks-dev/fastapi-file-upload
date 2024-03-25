from uuid import uuid4, UUID

import uvicorn

from fastapi import FastAPI, UploadFile, Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from src.sql import SessionLocal, engine
import src.schema, src.model

from model import Base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/file/", response_model=schema.FileModel)
def create_file(file: UploadFile, db: Session = Depends(get_db)):
    # Create DB model of file
    fmid = uuid4()
    file_model = model.FileModel(
        id=fmid,
        path=f'/home/{file.filename}'
    )

    # Save bytes
    with open(file_model.path, "wb") as bf:
        bf.write(file.file.read())
    
    # Save to DB
    db.add(file_model)
    db.commit()
    db.refresh(file_model)

    # Return schema (UUID only)
    return file_model

@app.get("/file/{id}")
def read_file(id: UUID, db: Session = Depends(get_db)):
    # Get DB model
    file_model = (
        db.query(model.FileModel)
        .filter(model.FileModel.id == id)
        .first()
    )

    # Get file at path
    return FileResponse(file_model.path)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="0.0.0.0",
        reload=False
    )
