import json
from git import get_commits
from gerrit import query_account

# print(get_commits('widget-alpha', author="wan", after="2022-07-01"))
print(query_account("tieenkai1"))
