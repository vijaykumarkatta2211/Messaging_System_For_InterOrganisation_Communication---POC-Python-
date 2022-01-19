from fastapi import APIRouter
from pydantic import BaseModel
from bson import ObjectId
import logging
from pymongo import MongoClient

conn = MongoClient()
user = APIRouter()

###########################################################BaseModels#####################################

class User(BaseModel):
     first_name: str
     last_name: str 
     org_name: str
     department: str
     user_email_id: str

#######################################################schemas############################################
def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "first_name":item["first_name"],  
        "last_name":item["last_name"], 
        "org_name":item["org_name"],
        "department":item["department"],
        "user_email_id":item["user_email_id"]
    }

def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]

############################################################logeer############################################

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("%(asctime)s -%(levelname)s -%(message)s")
fh = logging.FileHandler("UserLogfile.log" )
fh.setFormatter(f)

logger.addHandler(fh)

logger.info("Ready to onboard User")

#############################################################CRUD_Operations########################################

@user.get('/')
async def find_all_users():
    try:
        print(conn.local.user.find())
        logger.info("All users list ")
        logger.debug(usersEntity(conn.local.user.find()))
        return usersEntity(conn.local.user.find())
    except:
        logger.info("Please check server status")
        return("Please chack server status")

@user.get('/{id}')
async def find_one_user(id):
    try:
        logger.info("Details of User with id {}".format({"user_email_id":id}))
        logger.debug(userEntity(conn.local.user.find_one({"user_email_id":id})))
        return userEntity(conn.local.user.find_one({"user_email_id":id}))
    except:
        logger.info("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")
        return("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")

@user.post('/')
async def create_users(user: User):
    try:
        cd = dict(user)
        print(cd["user_email_id"])
        if conn.local.user.find_one({"user_email_id":cd["user_email_id"]}):
            return("User alredy exist")
        elif conn.local.org.find_one({"org_name":cd["org_name"]}):
            conn.local.user.insert_one(dict(user))
            logger.info("new user onboarded")
            return usersEntity(conn.local.user.find())
        return("Orgnaization not found")
        
    except:
        logger.info("Please check server status")
        return("Please check server status")

@user.put('/{id}')
async def update_user(id, user:User):
    try:
        cd = dict(user)
        if conn.local.org.find_one({"org_name":cd["org_name"]}):
         if conn.local.user.find_one_and_update({"user_email_id":id},{
            "$set":dict(user)
         }):
                logger.info("Details of User with id {} is updated".format({"user_email_id":id}))
                logger.debug(usersEntity(conn.local.user.find()))
                return usersEntity(conn.local.user.find())
        logger.info("please check Given Org_Id, Details Not found!!")
        return("please check Given Org_Id, Details Not found!!")
    except:
        logger.info("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")
        return("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")

@user.delete('/{id}')
async def delete_user(id):
    try:
        if conn.local.user.find_one_and_delete({"user_email_id":id}) is not None:
            logger.info("User with {} id is deleted ".format(id))
            return ("user of id {} deleted successfully".format(id))
        logger.info("please check Given Org_Id, Details Not found!!")
        return("please check Given Org_Id, Details Not found!!")
    except:
        logger.info("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")
        return("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")

        

