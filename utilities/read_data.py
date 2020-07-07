import csv

def getCSVData(fileName):

    #create an empty list to store rows
    rows=[]
    #open csv file
    dataFile=open(fileName,"r")
    #create a CSV Reader  from CSV file
    reader=csv.reader(dataFile)
    #skip headers
    next(reader)
    #add rows from reader to list
    for row in reader:
        rows.append(row)

    return rows
