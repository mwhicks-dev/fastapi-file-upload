# fastapi-file-upload
Demo to try and figure out how to do file uploads over FastAPI

Build:
```bash
docker build -t fileupload_demo .
```

Run:
```bash
docker run -d --rm \
-e POSTGRES_ADDRESS=${POSTGRES_ADDRESS} \
-e POSTGRES_DB=${POSTGRES_DB} \
-e POSTGRES_USER=${POSTGRES_USER} \
-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
-p 8000:8000 \
fileupload_demo
```