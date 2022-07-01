import requests
from consts import HOST
from config import auth
from utility import resp2json, querystring, urlencode

request_header = {'Content-Type': 'application/json'}


def query_changes(project: str, branch: str = "", status: str = "", owner: str = "", after: str = ""):
    '''
    :param project:
    :param branch:
    :param status:
    :param owner:
    :param after: 2006-01-02[ 15:04:05[.890][ -0700]]
    :return:
    '''

    info = {'project': project}
    if branch != '':
        info['branch'] = branch
    if status != '':
        info['status'] = status
    if owner != '':
        info['owner'] = owner
    if after != '':
        info['after'] = after
    q = querystring(info)
    response = requests.get(f'{HOST}/a/changes/?q={q}&n=25', auth=auth())
    return resp2json(response)


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
    response = requests.post(f'{HOST}/a/projects/{urlencode(project)}/commits/{commit}/cherrypick',
                             auth=auth(), json=data,
                             headers=request_header)
    return resp2json(response)


print(cherry_pick("platform/packages/apps/PersonalAssistant", '3ac8a07feb182a70c8a82e7d915e9e2435ee8f36',
                  "widget-alpha-L18"))
# print(json.dumps(query_changes("platform/packages/apps/PersonalAssistant", owner="wangxinpeng1", branch='widget-alpha'), indent=4))
