# Testing

Build:
```bash
docker build -t fileupload_demo/test .
```

Run:
```bash
docker run --rm \
-e POSTGRES_ADDRESS=${POSTGRES_ADDRESS} \
-e POSTGRES_DB=${POSTGRES_DB} \
-e POSTGRES_USER=${POSTGRES_USER} \
-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
fileupload_demo/test
```