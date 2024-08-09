import time

import client.models
from client import Client
from client.api.authentication import sign_in
from client.models.body_sign_in import BodySignIn
from client.models.token import Token
from client.types import Response

# client = Client(base_url="https://arqan.softeam-rd.eu/")


# from client.models.token import Token as Tokent

token = Token(access_token="")

cl = Client(base_url="https://arqan.softeam-rd.eu/", verify_ssl=False)

with cl as client:
    body = BodySignIn(username="test123", password="test123-")
    token = sign_in.sync(client=client, body=body)
    # or if you need more info (e.g. status_code)
    # response: Response[Token] = sign_in_api_auth_sign_in_post.sync_detailed(client=client, body=body)
    # print(response)

# print(token)


from client import AuthenticatedClient

acl = AuthenticatedClient(
    base_url="https://arqan.softeam-rd.eu/", token=token.access_token, verify_ssl=False
)

from app.client.api.common.get_task import sync as tasksync
from app.client.api.common.get_task import (
    sync_detailed as tasksync_detailed,
)
from client.api.stig_search import (
    search_db as stigsearch,
)
from client.models.request_search_db import SearchDBRequest


# Function to wait for task completion
def wait_for_task_completion(client, task_id, delay=0.1):
    while True:
        result = tasksync(client=client, task_id=task_id)
        if result is not None:
            return result
        time.sleep(delay)


with acl as cl:
    b = SearchDBRequest(text="Wireless Password Protect", platform="windows_10")
    r = stigsearch.sync(client=acl, body=b)
    tid = r["task_id"]
    print(tid)

    # r2: Response = tasksync_detailed(client=acl, task_id=r["task_id"])
    r2 = wait_for_task_completion(acl, tid, 0.1)

    # tid = "3abb52b0-1297-40de-96bb-0f54a94e5bae"
    # r2 = tasksync(client=acl, task_id=tid)

    print(r2)
