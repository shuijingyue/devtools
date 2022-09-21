import csv

with open('changes.log', 'r', encoding="utf-8") as changes:
    file = open('changes.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)
    
    for line in changes.readlines():
        writer.writerow(line.strip().split('|||'))
