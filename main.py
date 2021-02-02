import csv
import datetime
datetime_object = datetime.datetime.now()

f = open('file.txt')

with open('gebruik.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    line = f.readline()
    while line:
        writer.writerow(["01-02-2021 00:00","IJS06-0334","Handmatig blok 1",int(line)]) 
        line = f.readline()
f.close()
