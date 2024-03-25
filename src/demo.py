from uuid import uuid4, UUID

import uvicorn

from fastapi import FastAPI, UploadFile, Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from src.sql import SessionLocal, engine
from src.schema import FileModel as file_schema
from src.model import Base, FileModel as file_model

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/file/", response_model=file_schema)
def create_file(file: UploadFile, db: Session = Depends(get_db)):
    # Create DB model of file
    fmid = uuid4()
    model = file_model(
        id=fmid,
        path=f'/home/{file.filename}'
    )

    # Save bytes
    with open(model.path, "wb") as bf:
        bf.write(file.file.read())
    
    # Save to DB
    db.add(model)
    db.commit()
    db.refresh(model)

    # Return schema (UUID only)
    return model

@app.get("/file/{id}")
def read_file(id: UUID, db: Session = Depends(get_db)):
    # Get DB model
    model = (
        db.query(file_model)
        .filter(file_model.id == id)
        .first()
    )

    # Get file at path
    return FileResponse(model.path)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="0.0.0.0",
        reload=False
    )
