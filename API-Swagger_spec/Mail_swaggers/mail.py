import re
from fastapi import APIRouter
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
import logging

conn = MongoClient()
mail = APIRouter()
###########################################################Basemodules################################################################
class Mail(BaseModel):
    org_id: str
    to_user_id : str
    from_user_id: str
    mail_msg: str
##################################################schemas#####################################################
def mailEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "org_id":item["org_id"],
        "to_user_id" :item["to_user_id"],
        "from_user_id": item["from_user_id"],
        "mail_msg":item["mail_msg"]
    }

def mailsEntity(entity) -> list:
    return[mailEntity(item) for item in entity]
#########################################logeer#######################################################################

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("%(asctime)s -%(levelname)s -%(message)s")

fh = logging.FileHandler("file.log")
fh.setFormatter(f)

logger.addHandler(fh)
#logging.basicConfig(filename="application.log", level=logging.DEBUG , format="%(asctime)s"-"%(levelname)s")

logger.info("Start of mailbox logger")
########################################################urlOperation####################################################################


@mail.get('/')
async def find_all_mails():
    try:
        print(conn.local.mail.find())
        print(mailsEntity(conn.local.mail.find()))
        logger.info("All mails details list ")
        logger.debug(mailsEntity(conn.local.mail.find()))
        return mailsEntity(conn.local.mail.find())
    except:
        logger.info("Please check server status")
        return("Please check server status")

@mail.get('/{id}')
async def find_one_mail(id):
    try:
        logger.info("Details of mail with user id {}".format(id))
        logger.info(mailEntity(conn.local.mail.find_one({"from_user_id": id})))
        return mailEntity(conn.local.mail.find_one({"from_user_id": id}))
    except:
        logger.info("Please chack and enter correct Id, ID NOT FOUND")
        return("Please check and enter correct Id, ID NOT FOUND")

@mail.post('/')
async def mail_details(mail: Mail):
    try:
        cd = dict(mail) 
        if conn.local.user.find({"user_email_id":cd["from_user_id"]}):
            if conn.local.user.find({"user_email_id":cd["to_user_id"]}):
                if conn.local.org.find_one({"org_id":cd["org_id"]}):
                    conn.local.mail.insert_one(dict(mail))
                    logger.info("New mail request send")
                    return mailsEntity(conn.local.mail.find())
                return("Organisation Not Found , please enter Valide Org_ID")
        return("Please enter correct Email address")
    except:
        logger.info("Please check server status")
        return("Please check server status")

@mail.delete('/{id}')
async def delete_mail_details(id):
    try:
        logger.warning("New mail delete request send for:{} ".format(id))
        c = conn.local.mail.find_one_and_delete({"from_user_id": id})
        if c is not None:
            logger.info("Mail Deleted successfully")
            return("Mail Deleted successfully")
        logger.info("Details not found, please check ID !!!")
        return("Details not found, please check ID !!!")
    except:
        logger.info("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")
        return("Please check info 1:enter correct Id, DETAILS NOT FOUND, 2:Server Status ")

