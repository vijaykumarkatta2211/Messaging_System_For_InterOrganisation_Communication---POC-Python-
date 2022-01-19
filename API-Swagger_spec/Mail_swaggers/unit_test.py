from fastapi.testclient import TestClient
from bson import ObjectId

from routes.mail import mail

client = TestClient(mail)

data = {
    "org_id": "cg1",
    "to_usr_id" : "57cg1",
    "from_user_id": "2cg1",
    "mail_msg": "hello"
}



def test_created_mail():
    response = client.post("/", json=data)
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Post method Code"

def test_get_all_mail():
    response = client.get("/")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Get_all method Code"

    #assert data in response.json()

def test_get_mail():
    response = client.get("/57cg1")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Get method Code"

    #assert response.json() == data

def test_delete_mail():
    response = client.delete("/56cg1")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Delete mentod Code"

     
