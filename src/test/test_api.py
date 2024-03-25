from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_read_write_main():
    # POST file
    response = client.post(
        "/file/",
        files={"file": open("/home/src/test/media/ncsu.png", "rb")}
    )
    assert response.status_code == 200
    uuid = response.json()["id"]

    # GET file
    response = client.get(
        f"/file/{uuid}"
    )
    assert response.status_code == 200
    with open("/home/src/test/media/ncsu.png", "rb") as bf:
        assert response.read() == bf.read()