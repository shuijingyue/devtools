from entry.utilities import change_link, username
from gerrit import query_changes
import csv


#PAD 0625 # l18 0620

changes = query_changes(
    project="platform/packages/apps/PersonalAssistant", 
    branch="widget-alpha-L18",
    status="merged",
    after="2022-07-09")

with open('dist/result.csv', 'w', newline='') as fd:
    writer = csv.writer(fd)
    writer.writerow(['subject', 'link', 'owner'])
    for change in changes:
        writer.writerow([change.get('subject'), change_link(change), username(change)])

print('finish')
