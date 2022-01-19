from datetime import date
from models.user import User


def get_registered_user():
    return {
        "welcomeMsg": User.org_name,
        "to":User.name,
        "displayName" : User.name,
        "email" : User.name+"@altran.com"
            }
def send_message_user():
    today = date.today()
    return {
    "arraivalTime" : today,
    "subject" : "onboarded message from altran",
    "msg" : "congratulations for joining us..",
    "from" : "altran",
    "displayName":"ALTRAN",
    "email " : "it@altran.com",

    "to" : "",
        "displayName":"vijayKumar",
        "email" : "vijay@altran.com"
    }
if __name__ == "__main__":
    print(get_registered_user())
    print(send_message_user())
