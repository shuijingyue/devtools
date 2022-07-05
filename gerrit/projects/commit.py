import requests
from config import auth
from gerrit.consts import HOST
from gerrit.utility import resp2json, urlencode


def cherry_pick(project, commit, destination):
    '''
    /projects/{project-name}/commits/{commit-id}/cherrypick
    :param project:
    :param commit:
    :param destination:
    :return:
    '''
    data = {
        'destination': destination,
        'allow_conflicts': True
    }
    request_header = {'Content-Type': 'application/json'}

    response = requests.post(f'{HOST}/a/projects/{urlencode(project)}/commits/\
{commit}/cherrypick',
                             auth=auth(), json=data,
                             headers=request_header)
    return resp2json(response)
