import json
import urllib.parse
import requests


def resp2json(response: requests.Response):
    if response.ok:
        return json.loads(response.text[5:])
    else:
        print("============gerrit response============")
        print(response.headers)
        print(response.text)
        return None


def querystring(obj: dict):
    q = []
    for key, value in obj.items():
        q.append(f'{key}:{value}')
    return '+'.join(q)


def urlencode(s: str):
    return urllib.parse.quote(s, safe='')
