from fastapi import APIRouter
from pydantic import BaseModel
from bson import ObjectId
import logging
from pymongo import MongoClient

conn = MongoClient()
org = APIRouter()
###########################################################Basemodules########################################################################

class Org(BaseModel):
     org_name: str
     org_id: str
     org_email: str

############################################################schemas############################################################################

def orgEntity(item) -> dict:
    return{
        "id":str(item["_id"]), 
        "org_name":item["org_name"],
        "org_id":item["org_id"],
        "org_email":item["org_email"]
    }

def orgsEntity(entity) -> list:
    return[orgEntity(item) for item in entity]

############################################################logger##############################################################################
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("%(asctime)s -%(levelname)s -%(message)s")
fh = logging.FileHandler("orgLogfile.log" )
fh.setFormatter(f)

logger.addHandler(fh)

logger.info("Ready to onboard Org")
#############################################################CRUD_Operation###################################################################################
@org.get('/')
async def find_all_orgs():
    try:
        #print(conn.local.org.find())
        logger.info("All Orgs list ")
        logger.debug(orgsEntity(conn.local.org.find()))
        return orgsEntity(conn.local.org.find())
    except:
        return("There is no any org")

@org.get('/{id}')
async def find_one_org(id):
    try:
        logger.info("Finding Details of Specifice org based on object id")
        logger.debug(orgEntity(conn.local.org.find_one({"org_id":id})))
        return orgEntity(conn.local.org.find_one({"org_id":id}))
    except:
        logger.info("Please check and enter correct Id, ID NOT FOUND!!!!")
        return("Please check and enter correct Id, ID NOT FOUND!!!!")

@org.post('/')
async def create_orgs(org: Org):
    try:
        conn.local.org.insert_one(dict(org))
        logger.info("New org onboarded")
        return orgsEntity(conn.local.org.find())
    except:
        logger.info("Please chack server status")
        return("Please chack server status")

@org.put('/{id}')
async def update_org(id,org: Org):
    try:
        if conn.local.org.find_one_and_update({"org_id":id},{
            "$set":dict(org)
        }) is not None:
            logger.info("Org details updated for given object Id")
            logger.debug(orgsEntity(conn.local.org.find()))
            return orgsEntity(conn.local.org.find())
        logger.info("please check Given Org_Id, Details Not found!!")
        return("please check Given Org_Id, Details Not found!!")
    except:
        logger.info("please check 1:Given Org_Id, 2:server status")
        return("please check 1:Given Org_Id, 2:server status")

@org.delete('/{id}')
async def delete_org(id):
    try:
        c = conn.local.org.find_one_and_delete({"org_id":id})
        logger.info(c)
        if c is not None:
            logger.info("Org with id {} is deleted ".format(id))
            return("Org of id {} deleted successfully".format(id))
        logger.info("please check Given Org_Id, Details Not found!!")
        return("please check Given Org_Id, Details Not found!!")
    except:
        logger.info("please check 1:Given Org_Id, 2:server status")
        return("please check 1:Given Org_Id, 2:server status")

@org.delete('/user/{U_id}')
async def delete_user(U_id):
    try:
        c = conn.local.user.find_one_and_delete({"user_email_id":U_id})
        if c is not None:
            logger.info("User with {} id is deleted ".format(U_id))
            return ("user of id {} deleted successfully".format(U_id))
        logger.info("please check Given User_Id, Details Not found!!")
        print(U_id)
        return("please check Given User_Id, Details Not found!!{U_id}")
    except:
        logger.info("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")
        return("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")



