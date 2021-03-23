from skpy import Skype
from skpy import SkypeEventLoop

GROUP_CHAT_ID="[group id where your bot belong]"
USER_ID="[skype bot user id]"
USER_PASS="[skype bot password]"
USER_RESOURCE="[skype bot resource]"

#user_resource can be got from event.__dict__.get('raw').get('resource').get('from') when your user bot sent message

class MySkype(SkypeEventLoop):
    
    def onEvent(self, event):
        DICT_RESPONSE={
        "How are you":"Fine",
        "Thank you":"You're welcome", 
        "Halo":"Hai"
        #add more here..
        }

        condition_1=event.type=="NewMessage"
        condition_2='msgId' in event.__dict__.keys()
        condition_3=(event.__dict__.get('raw').get('resource').get('from') != USER_RESOURCE)

        if(condition_1 and condition_2 and condition_3):
            self.chats[GROUP_CHAT_ID].sendMsg(DICT_RESPONSE.get(event.msg.content,"Wrong Keyword!!"))

if __name__ == "__main__":
    sk = MySkype(USER_ID, USER_PASS, autoAck=True)
    sk.loop()