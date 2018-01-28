from flask import json
from flask import jsonify
from twilio.rest import Client
from random import randint

def emoji_generator():
    hand_emoji = ""
    randnumb = randint(0,5)
    if randnumb == 0:
        hand_emoji = u"\U0001F44C"
    elif randnumb == 1:
        hand_emoji = u"\U0001F44D"
    elif randnumb == 2:
        hand_emoji = u"\U0001F44F"
    elif randnumb == 3:
        hand_emoji = u"\U0001F450"
    elif randnumb == 4:
        hand_emoji = u"\U0001F44B"
    elif randnumb == 5:
        hand_emoji = u"\U0001F4AA"

    return hand_emoji


def send_sms(contactName, contactNumber, relationToContact, tone):
    # Your Account SID from twilio.com/console
    account_sid = "ACcf91bd017602f73edd23a347f79f1056"
    # Your Auth Token from twilio.com/console
    auth_token  = "9162aefa6990c34794081548e1baa02f"

    client = Client(account_sid, auth_token)


    bodyToSend = ""

    if tone is "angry":
        bodyToSend = u"\U0001F648\U0001F648\U0001F649\U0001F649 Hey there {0}, it seems \U0001F624\U0001F624 that \U0001F624\U0001F624 your \U0001F60D\U0001F60D {1} \U0001F60D\U0001F60D is \U0001F621\U0001F621\U0001F621 angry \U0001F621, maybe you should \U0001F914\U0001F914 call that person fam \U0001F914\U0001F914{2}".format(contactName, relationToContact, emoji_generator())
    if tone is "fear":
        bodyToSend = u"\U0001F617\U0001F617 Hey {0}, your {1} may be feeling scared right now \U0001F631\U0001F631, maybe you should \U0001F5E3 call \U0001F5E3 that person dawg \U0001F436".format(contactName ,relationToContact)
    if tone is "sadness":
        bodyToSend = u"\U0001F575\U0001F575 Pssst, {0} I think your {1} is feeling sad \U0001F622\U0001F622 today, I'd be great \U0001F622\U0001F622 if you let that \U0001F46A person \U0001F46A know that you're thinking of  \U0001F618 them \U0001F618".format(contactName, relationToContact)

    message = client.messages.create(
                to="+{0}".format(contactNumber),
                from_="+16474923577",
                body=bodyToSend
    )

    print(message.sid)