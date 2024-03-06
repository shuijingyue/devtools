import csv
import datetime

import git


def diff():
    with open('changes.log', 'r', encoding="utf-8") as changes:
        file = open('changes.csv', 'w', encoding="utf-8", newline='')
        writer = csv.writer(file)

        for line in changes.readlines():
            writer.writerow(line.strip().split('|||'))


if __name__ == '__main__':
    git.extract_jiras('/Users/shihuan/Workspace/miui/MiuiAod',
                      int(datetime.datetime(year=2023, month=9, day=6).timestamp()))
