import csv
data = []
i = 0
with open("classUserStast.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			data.append(row)
		i += 1