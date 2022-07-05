import requests
from config import auth
from gerrit.consts import HOST
from gerrit.utility import resp2json, querystring


def query_changes(project: str, branch: str = "", status: str = "",
                  owner: str = "", after: str = ""):
    '''
    /changes/?q={q}
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
        info['mergedafter'] = after
    q = querystring(info)
    response = requests.get(f'{HOST}/a/changes/?q={q}&no-limit', auth=auth())
    return resp2json(response)
