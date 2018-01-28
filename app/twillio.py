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

# dictOfTone = {
#   "document_tone": {
#     "tones": [
#       {
#         "score": 0.6165,
#         "tone_id": "sadness",
#         "tone_name": "Sadness"
#       },
#       {
#         "score": 0.829888,
#         "tone_id": "analytical",
#         "tone_name": "Analytical"
#       }
#     ]
#   },
#   "sentences_tone": [
#     {
#       "sentence_id": 0,
#       "text": "Team, I know that times are tough!",
#       "tones": [
#         {
#           "score": 0.801827,
#           "tone_id": "analytical",
#           "tone_name": "Analytical"
#         }
#       ]
#     },
#     {
#       "sentence_id": 1,
#       "text": "Product sales have been disappointing for the past three quarters.",
#       "tones": [
#         {
#           "score": 0.771241,
#           "tone_id": "sadness",
#           "tone_name": "Sadness"
#         },
#         {
#           "score": 0.687768,
#           "tone_id": "analytical",
#           "tone_name": "Analytical"
#         }
#       ]
#     },
#     {
#       "sentence_id": 2,
#       "text": "We have a competitive product, but we need to do a better job of selling it!",
#       "tones": [
#         {
#           "score": 0.506763,
#           "tone_id": "analytical",
#           "tone_name": "Analytical"
#         }
#       ]
#     }
#   ]
# }
# jsonOfTone = json.dumps(dictOfTone)

def get_tone(jsonFromToneAnalyzer):
    eldersTone = ""
    tonesDict = json.loads(jsonFromToneAnalyzer)["document_tone"]["tones"]
    # print tonesDict
    for tones in tonesDict:
        if ((tones["tone_id"] == "sadness") or
                (tones["tone_id"] == "angry") or
                (tones["tone_id"] == "fear")) and (tones["score"] > 0.60):
            eldersTone = tones["tone_id"]

    print 'eldertone ',eldersTone
    return eldersTone

# get_tone(jsonOfTone)




def send_sms(targetNumber, relationToContact, tone):
    # Your Account SID from twilio.com/console
    account_sid = "ACcf91bd017602f73edd23a347f79f1056"
    # Your Auth Token from twilio.com/console
    auth_token  = "9162aefa6990c34794081548e1baa02f"

    client = Client(account_sid, auth_token)


    bodyToSend = ""

    if tone is "angry":
        bodyToSend = u"\U0001F648\U0001F648\U0001F649\U0001F649 Hey there, it seems \U0001F624\U0001F624 that \U0001F624\U0001F624 your \U0001F60D\U0001F60D {0} \U0001F60D\U0001F60D is \U0001F621\U0001F621\U0001F621 angry \U0001F621, maybe you should \U0001F914\U0001F914 call that person fam \U0001F914\U0001F914{1}".format(relationToContact, emoji_generator())
    if tone is "fear":
        bodyToSend = u"\U0001F617\U0001F617 Your {0} may be feeling scared right now \U0001F631\U0001F631, maybe you should \U0001F5E3 call \U0001F5E3 that person dawg \U0001F436".format(relationToContact)
    if tone is "sadness":
        bodyToSend = u"\U0001F575\U0001F575 Pssst, I think your {0} is feeling sad \U0001F622\U0001F622 today, I'd be great \U0001F622\U0001F622 if you let that \U0001F46A person \U0001F46A know that you're thinking of  \U0001F618 them \U0001F618".format(relationToContact)
    message = client.messages.create(
                to="+{0}".format(targetNumber),
                from_="+16474923577",
                body=bodyToSend
    )

    print(message.sid)