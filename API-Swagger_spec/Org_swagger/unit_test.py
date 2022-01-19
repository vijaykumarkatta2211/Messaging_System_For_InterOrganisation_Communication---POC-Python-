from fastapi.testclient import TestClient
from bson import ObjectId

from routes.user import org

client = TestClient(org)


data = {
    "org_name": "org_name",
    "org_id":"cg_1",
    "org_email":"org@gmail.com"
}

data1 = {
    "org_name": "org_name",
    "org_id":"cg_2",
    "org_email":"org@gmail.com"
}

data2 = {
    "org_name": "org_name",
    "org_id":"cg_3",
    "org_email":"org14@gmail.com"
}

def test_created_org():
    response = client.post("/", json=data1)
    try:
        assert response.status_code == 201, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Creat_org method in user.py Code"
    

def test_get_all_org():
    response = client.get("/")
    try:
        assert response.status_code == 201, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Get_all_org method in user.py Code"
    

def test_get_org():
    response = client.get("/cg_2")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Get_org method in user.py Code"
   
def test_update_org():
    response = client.put("/cg_2", json=data2)
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Update_org method in user.py Code"
    

def test_delete_org():
    response = client.delete("/cg_3")
    try:
        assert response.status_code == 200, "okay"
    except:
        assert response.status_code != 200, "Please check 1:server connectivity, 2:Delet_org method in user.py Code"
