import requests
from config import auth
from gerrit.consts import HOST
from gerrit.utility import resp2json


def get_commit(change_id, revision_id):
    '''
    /changes/{change-id}/revisions/{revision-id}/commit'
    '''
    respose = requests.get(f'{HOST}/a/changes/{change_id}/revisions/\
{revision_id}/commit', auth=auth())
    return resp2json(respose)
