import csv
from operator import itemgetter
#data = []
i = 0
header = []
userPushes = {}
data = []
with open("m_2784-3783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			data.append([str(i),row[1],row[2],row[3],row[4],row[5]])
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [str(i)]
			else:
				userPushes[row[1]].append(str(i))

		i += 1
j = 0
with open("pushesHPall_2752-2783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if j == 0:
			header = row
		else:
			data.append([str(i),row[1],row[2],row[3],row[4],row[5]])
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [str(i)]
			else:
				userPushes[row[1]].append(str(i))

			i += 1
		j += 1

with open("m_2752-3783.csv", "w", newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	for row in data:
		writer.writerow(row)

d = []

for u in userPushes.keys():
	val = ",".join(userPushes[u])
	d.append([str(u),len(userPushes[u]),val])

data_ = sorted(d, key=itemgetter(1), reverse=True)

with open("m_stats2752-3783.csv", "w", newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(["id", "amount", "contentIDs"])
	'''
	for i in userPushes.keys():
		val = ",".join(userPushes[i])
		writer.writerow([str(i),len(userPushes[i]),val])
	'''
	for dd in data_:
		writer.writerow(dd)

#newD = sorted(userPushes.keys(), key=lambda k: len(userPushes[k]), reverse=True)
#print(userPushes)