import json
from gerrit.consts import HOST


with open('dist/accounts.json', 'r') as fd:
    accounts = json.load(fd)

def subject2change(changes):
    ret = {}
    for change in changes:
        ret[change.get('subject')] = change
    return ret


def username(change):
    id = change.get('owner').get('_account_id')
    return accounts.get(str(id))


def change_link(change):
    return f'{HOST}/c/{change.get("project")}/+/{change.get("_number")}'
