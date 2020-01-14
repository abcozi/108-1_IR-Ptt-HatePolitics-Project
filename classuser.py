import csv

i = 0
user = []
userStats = []
with open("m_stats2752-3783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			user.append([row[0]])
			userStats.append([row[0],0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		i += 1
for u in user:
	subr = []
	for k in range(14):
		subr.append([])
	u.append(subr)
#print(user[0][1][13])
#print(userStats[0])
i = 0
data = []
header = []
#userClasses = {}
with open("filtLabels.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			for u in user:
				if u[0] == row[1]:
					
					labs = row[-1].split(" ")
					#print(labs)
					for l in labs:
						if l.isnumeric():
							v = int(l)
							u[1][v-1].append(row[0])
		i += 1
		if i >0 and i % 2000 == 0:
			print(i)
j = 0
with open("classUserStast.csv", "w", newline='') as csvfile:
	print("write to classUserStast.csv......")
	writer = csv.writer(csvfile)
	writer.writerow(["id","len1","len2","len3","len4","len5","len6","len7","len8","len9","len10",\
		"len11","len12","len13","len14","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10",\
		"c11","c12","c13","c14"])
	for u in user:
		row = []
		row.append(u[0])
		for jj in range(14):
			row.append(len(u[1][jj]))
		for jj in range(14):
			row.append(u[1][jj])
		writer.writerow(row)
		j += 1
		print("j: "+str(j))
		print(row)
	print("wrote to classUserStast.csv......")
'''		
with open("classUserData.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["id","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10",\
		"c11","c12","c13","c14"])
	for u in user:
		write.writerow()
'''