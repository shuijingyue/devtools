from config import auth
from gerrit.utility import resp2json, urlencode
from gerrit.consts import HOST
import requests


def list_branches(project):
    '''
     /projects/{project-name}/branches/
    '''
    response = requests.get(f'{HOST}/a/projects/{urlencode(project)}/branches',
                            auth=auth())
    return resp2json(response)


def get_branch(project, branch):
    '''
    /projects/{project-name}/branches/{branch-id}
    '''
    response = requests.get(f'{HOST}/a/projects/{urlencode(project)}/branches/\
{branch}',
                            auth=auth())
    return resp2json(response)


def branch_reflog(project, branch):
    '''
    /projects/{project-name}/branches/{branch-id}/reflog
    '''
    response = requests.get(f'{HOST}/a/projects/{urlencode(project)}/branches/\
{branch}/reflog',
                            auth=auth())
    return resp2json(response)
