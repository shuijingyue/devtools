from entry.utilities import change_link, subject2change, username
from gerrit import query_changes
import csv


source_changes = query_changes(
    project="platform/packages/apps/PersonalAssistant", 
    branch="widget-alpha",
    status="merged",
    after="2022-06-01")

source_map = subject2change(source_changes)

target_changes = query_changes(
    project="platform/packages/apps/PersonalAssistant", 
    branch="widget-alpha-PAD",
    status="merged",
    after="2022-06-01")

target_map = subject2change(target_changes)

with open('dist/result.csv', 'w', newline='') as fd:
    writer = csv.writer(fd)
    writer.writerow(['subject', 'link', 'owner'])
    for (key,value) in source_map.items():
        if target_map.get(key) is None:
            writer.writerow([key, change_link(value), username(value)])
print('finish')
