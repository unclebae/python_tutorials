import csv
import os

dirPath = "../files"
filePath = "test.csv"
if (os.path.exists(dirPath) is False) :
    os.makedirs(dirPath)

if (os.path.exists(dirPath + filePath) is False) :
    print(dirPath + filePath + " not exists.")

csvFile = open(dirPath + filePath, "w+")

try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow( (i, i+2, i*2))
finally:
    csvFile.close()