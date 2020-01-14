import csv
from operator import itemgetter
i = 0
data = []
header = []
with open("m_sorted_stats3266-3783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			data.append([row[0], int(row[1]), row[2]])
		i += 1
print(str(len(data))+", i: "+str(i))
data_ = sorted(data, key=itemgetter(1), reverse=True)
print(data_[0])
with open("m_sorted2_stats3266-3783.csv", 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	for row in data_:
		writer.writerow(row)