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
