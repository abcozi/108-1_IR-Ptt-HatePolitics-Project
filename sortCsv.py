import csv
with open('m_stats3266-3783.csv',newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row:(row['amount']), reverse=True)


with open('m_sorted_stats3266-3783.csv', 'w') as f:
    fieldnames = ['id', 'amount', 'contentIDs']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in sortedlist:
        writer.writerow(row)