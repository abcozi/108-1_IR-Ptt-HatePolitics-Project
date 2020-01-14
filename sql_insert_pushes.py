import csv
'''
INSERT INTO table_name
VALUES ("value1_1, value2_2, value3_3,···),
(value2_1, value2_2, value2_3,···),
(value3_1, value3_2, value3_3,···),
'''

i = 0
data = []
with open("m_2784-3783.csv", newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if i == 0:
			header = row
		else:
			data.append(row)
		i += 1
print("i: "+str(i))
run = int(i/50000) + 1
print("run: "+str(run))
for k in range(run):
	j = 0 + k*50000
	table_name = "test"
	query = "INSERT INTO `"+table_name+"` VALUES"
	thisFrom = int(0 + k*50000)
	thisTo = int((k+1)*50000-1)
	if k == run-1:
		thisTo = len(data)-1
	print("thisFrom: "+str(thisFrom)+", thisTo: "+str(thisTo))
	while j >= thisFrom and j < thisTo:
		query += "(\""+str(data[j][0])+"\", \""+str(data[j][1])+"\", \""+str(data[j][2])+\
			"\", \""+str(data[j][3])+"\", \""+str(data[j][4])+"\", \""+str(data[j][5])+"\"),"
		j += 1
	last = "(\""+str(data[j][0])+"\", \""+str(data[j][1])+"\", \""+str(data[j][2])+\
			"\", \""+str(data[j][3])+"\", \""+str(data[j][4])+"\", \""+str(data[j][5])+"\");"
	query += last
	print("j: "+str(j))
	print("last: "+last)
	with open("sql_insert_pushes3-"+str(k+1)+".txt", "w") as f:
		f.write(query)
