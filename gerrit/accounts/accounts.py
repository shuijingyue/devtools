import json
import requests
from config import auth
from gerrit.consts import HOST
from gerrit.utility import resp2json


def query_account(username: str) -> dict:
    '''
    /accounts/?q=name:John+email:example.com&n=2
    '''
    response = requests.get(f'{HOST}/a/accounts/?q=name:{username}',
                            auth=auth())
    return resp2json(response)[0]
