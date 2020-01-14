import csv
from operator import itemgetter
#data = []
i = 0
header = []
userPushes = {}
data = []
with open("m_3266-3783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])

		i += 1
i = 0
with open("pushesHPall_3248-3265.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])

		i += 1
i = 0
with open("pushesHPall_3231-3247.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])
		i += 1
i = 0
with open("pushesHPall_3158-3230.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])
		i += 1
i = 0
with open("pushesHPall_2956-3157.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])
		i += 1
i = 0
with open("pushesHPall_2946-2955.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])
		i += 1
i = 0
with open("pushesHPall_2942-2945.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])
		i += 1
i = 0
with open("pushesHPall_2916-2941.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			pass
		else:
			data.append(row)
			if row[1] not in userPushes.keys():
				userPushes[row[1]] = [row[0]]
			else:
				userPushes[row[1]].append(row[0])
		i += 1

with open("m_2916-3783.csv", "w", newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	for row in data:
		writer.writerow(row)

d = []
j = 0

for u in userPushes.keys():
	val = ",".join(userPushes[u])
	d.append([str(u),len(userPushes[u]),val])

data_ = sorted(d, key=itemgetter(1), reverse=True)

with open("m_stats2916-3783.csv", "w", newline='') as csvFile:
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