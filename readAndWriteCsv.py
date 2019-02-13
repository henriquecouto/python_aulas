import csv

medias = []
with open('aluno.csv', mode='r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		medias.append([row[0], row[1], row[2], row[3], (float(row[2])+float(row[3])) // 2])

with open('aluno.csv', mode='w') as csvfile:
	writeCSV = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in medias:
		writeCSV.writerow(row)