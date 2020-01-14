import csv
i = 0
data = []
header = []
with open("cut20000-1_label2.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			val = str(row[6])
			if val.isnumeric() is False or (val.isnumeric() and int(val) > 0):
				data.append(row)
		i += 1
j = 0
with open("cut20000-2_label2.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if j == 0:
			header = row
		else:
			val = str(row[6])
			if val.isnumeric() is False or (val.isnumeric() and int(val) > 0):
				data.append(row)
		j += 1
with open("filtLabels.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(header)
	for d in data:
		writer.writerow(d)
print("data len: "+str(len(data)))