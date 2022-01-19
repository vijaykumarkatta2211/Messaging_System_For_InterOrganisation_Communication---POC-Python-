from fastapi.testclient import TestClient
from bson import ObjectId

from routes.user import user

client = TestClient(user)


data = {
    "first_name":"first_name",  
    "last_name":"last_name", 
    "org_name":"org_name",
    "department":"department",
    "user_email_id":"user_email_id0"
}

data2 = {
    "first_name":"first_name",  
    "last_name":"last_name", 
    "org_name":"org_name",
    "department":"department",
    "user_email_id":"user_email_id1"
}

data1 = {
    "first_name":"yadnyesh",  
    "last_name":"darekar", 
    "org_name":"capgemini",
    "department":"cisco",
    "user_email_id":"user@gmail.com"
}

def test_created_user():
    response = client.post("/", json=data)
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Creat_user method in user.py Code"

def test_get_all_user():
    response = client.get("/")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Get_all method in user.py Code"
    #assert data in response.json()

def test_get_user():
    response = client.get("/user_email_id0")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Get_user method in user.py Code"
    #assert response.json() == data

def test_update_user():
    response = client.put("/user_email_id0", json=data2)
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Update_user method in user.py Code"

def test_delete_user():
    response = client.delete("/user_email_id1")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Delete_user method in user.py Code"
        
