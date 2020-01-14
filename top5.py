import csv
from operator import itemgetter
data = []
i = 0
with open("classUserStast.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			r = [row[0]]
			for k in range(14):
				r.append(int(row[k+1]))
			for k in range(14):
				r.append(row[k+15])
			data.append(r)
		i += 1
classNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for j in range(14):
	data_ = sorted(data, key=itemgetter(j+1), reverse=True)
	with open("top5_c"+str(j+1)+".csv", "w", newline='') as csvfile:
		print("write to "+"top5_c"+str(j+1)+".csv")
		writer = csv.writer(csvfile)
		writer.writerow(["id","len1","len2","len3","len4","len5","len6","len7","len8","len9","len10",\
			"len11","len12","len13","len14","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10",\
			"c11","c12","c13","c14"])
		for d in data_:
			writer.writerow(d)
			#print(d[j+1])
			classNum[j] += d[j+1]
print(classNum)