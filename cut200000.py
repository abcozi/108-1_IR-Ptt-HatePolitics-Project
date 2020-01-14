import csv
data = []
header = []
i = 0
with open("m_2752-3783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			data.append(row)
		i += 1
with open("cut20000-1.csv", "w", newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	for dd in data[:200000]:
		writer.writerow(dd)

with open("cut20000-2.csv", "w", newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	for dd in data[200000:]:
		writer.writerow(dd)
