import csv
import string

badlines=0
goodlines=0

#truncate words that are longer than maxlength and replace last 3 chars with ...
def removelongitems(datatable):
    newdatatable=[]
    maxlength = 20
    for row in datatable:
        newrow = []
        for item in row:
            if len(item) > maxlength:
                newitem = item[:maxlength-3] + "..."
            else:
                newitem = item
            newrow.append(newitem)
        newdatatable.append(newrow)
    return newdatatable

#remove characters in other languages, emojis, and more.
def removebadchars(datatable):
    newdatatable=[]

    for row in datatable:
        newrow = []
        for item in row:
            allowed_chars = string.ascii_letters + string.digits + string.punctuation + ' '
            filtereditem = ''.join(ch for ch in item if ch in allowed_chars)
            newrow.append(filtereditem)
        newdatatable.append(newrow)
    return newdatatable

#keep only rows with the correct number of values.
def keepgoodlines(datatable, perRow):
    global goodlines
    global badlines
    newdatatable=[]
    for i in range(0, len(datatable)):
        if(len(datatable[i])!=perRow):
            badlines+=1
        else:
            newdatatable.append(datatable[i])
            goodlines+=1
    print(badlines, "badline(s) discarded in the csv file selected.")
    print(goodlines, "goodline(s) provided in the csv file selected.")
    return newdatatable

#read the data and output it into a 2d list based off of the separator
def read_data(file, args):
    reader = csv.reader(file, delimiter = args.s)
    datatable = [row for row in reader]
    perRow = len(datatable[0])

    datatable = keepgoodlines(datatable, perRow)
    datatable = removebadchars(datatable)
    datatable = removelongitems(datatable)

    return datatable