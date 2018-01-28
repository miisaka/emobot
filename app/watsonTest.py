from watson_developer_cloud import ConversationV1
import json

conversation = ConversationV1(
    username = '48bdbc18-d849-450c-894d-e79de42e5a7f',
    password = 'HQDq5MCID6rW',
    version = '2017-05-26'
)

response = conversation.list_workspaces()

print(json.dumps(response, indent=2))

response = conversation.message(
    workspace_id='522f8bfa-610d-46d7-bd1c-85205cfd2b50',
    input={
        'text': 'hi'
    }
)

print(json.dumps(response, indent=2))