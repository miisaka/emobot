from watson_developer_cloud import ConversationV1
from watson_developer_cloud import ToneAnalyzerV3
import json
import os


conversation = ConversationV1(
    username='48bdbc18-d849-450c-894d-e79de42e5a7f',
    password='HQDq5MCID6rW',
    version='2017-05-26'
)

tone_analyzer = ToneAnalyzerV3(
  version='2017-09-21',
  username='a8802b67-2345-4cab-841a-4dede820f5e7',
  password='fn7VYBpDSVbb'
)


def conversationInput(input, workspace_number):

    if workspace_number == 1:
        workspace_id = '522f8bfa-610d-46d7-bd1c-85205cfd2b50'
    if workspace_number == 2:
        workspace_id = '25c08b66-e9f4-4275-ad4c-ca6b62dc9f9f'
    if workspace_number == 3:
        workspace_id = 'ca699c68-d8e1-4f81-a06b-a831dd425015'

    response = conversation.message(
        workspace_id=workspace_id,
        input={
            'text': input
        }
    )
    print(json.dumps(response, indent=2))

    return response


def toneInput(input):
    inputDict = {}
    inputDict['text'] = input
    with open('tone.json', 'w') as outfile:
        json.dump(inputDict, outfile)

    with open('./tone.json') as tone_json:
        tone = tone_analyzer.tone(tone_json.read())
    print(json.dumps(tone, indent=2))

    try:
        os.remove('./tone.json')
    except OSError:
        pass
    return tone


toneInput("I cried again today")


#get tone from json

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