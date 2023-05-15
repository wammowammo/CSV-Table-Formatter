from tabulate import tabulate
from data_reader import read_data
import sys

#for args.n
def listfirstrows(datatable, value):
    newdatatable=[]
    if(value > len(datatable)-1):
        print("requested more rows than there are, printing all rows.")
        return datatable
    for i in range(value+1):
        newdatatable.append(datatable[i])
    return newdatatable

#for args.m
def listcertainrows(datatable, value):
    newdatatable =[]
    newdatatable.append(datatable[0])
    added = False
    for row in datatable:
        if value in row:
            newdatatable.append(row)
            added=True
    if(not added):
        print(value+" not in the datatable")
    return newdatatable

#for args.d
def descendingsort(datatable, value):
    priority = {}
    if value not in datatable[0]:
        print(value+" not in the datatable header")
        return datatable
    else:
        columntosort = datatable[0].index(value)
    
    for row in range(1,len(datatable)):
        priority[row] = datatable[row][columntosort]
    
    sortedpriority={}
    for i in sorted(priority.values(), reverse=True):  # Adding reverse=True for descending order
        for j in priority.keys():
            if priority[j] == i:
                sortedpriority[j] = priority[j]
    newdatatable = []
    newdatatable.append(datatable[0])
    
    for key in sortedpriority.keys():
        newdatatable.append(datatable[key])
    return newdatatable

#for args.u
def ascendingsort(datatable, value):
    priority = {}
    if value not in datatable[0]:
        print(value+" not in the datatable header, listing in default order.")
        return datatable
    else:
        columntosort = datatable[0].index(value)
    
    for row in range(1,len(datatable)):
        priority[row] = datatable[row][columntosort]
    
    sortedpriority={}
    for i in sorted(priority.values()):
        for j in priority.keys():
            if priority[j] == i:
                sortedpriority[j] = priority[j]
    newdatatable = []
    newdatatable.append(datatable[0])
    
    for key in sortedpriority.keys():
        newdatatable.append(datatable[key])
    return newdatatable

#for args.o
def certaincolumns(datatable, args):
    columntoprint=[]
    for word in args.o:
        if word not in datatable[0]:
            print(word+" not in the datatable header")
        else:
            columntoprint.append(datatable[0].index(word))
    temp=[]
    temprow=[]
    for j in range(len(datatable)):
        for i in columntoprint:
            temprow.append(datatable[j][i])
        temp.append(temprow)
        temprow=[]
    return temp


#format the datatable (clean and whatever specifications user inputs)
def format_table(file, args):
    try:
        with open(file, 'r') as file:
            #takes the data, cleans it, puts it into file.
            datatable = read_data(file, args)
            if datatable == [['\ufeff']]: 
                sys.exit("Error: CSV file is empty. Please input a non-empty CSV file.")
            #if the table is only one row long you cannot provide further args.
            if len(datatable) == 1 and \
                            (args.s or args.u or args.d or args.m or args.n):
                sys.exit("Error: Cannot use -s, -u, -d, -m, or -n options with a"
                        " table containing only column headers.")
            #if the separator for the values also appears in one of the data categories.
            for row in datatable:
                for cell in row:
                    if args.s in cell:
                        sys.exit(f"Error: The separator '{args.s}' conflicts with"
                                f"characters in column names or cell values.")
            
            #only print out certain columns
            if(args.o):
                datatable=certaincolumns(datatable, args)

            #cannot have descending and ascending sort at the same time
            if(args.u and args.d):
                sys.exit("Error: cannot use ascending and descending sort together.")
            
            #ascending sort
            if(args.u):
                datatable=ascendingsort(datatable, args.u)
            
            #descending sort
            if(args.d):
                datatable=descendingsort(datatable, args.d)
            
            #only print a row if a value is present within it
            if(args.m):
                datatable=listcertainrows(datatable,args.m)
            
            #display the first n number of rows.
            if(args.n):
                datatable=listfirstrows(datatable,args.n)

            #only print the headers
            if(args.l): 
                for row in datatable:
                    print(tabulate([row], tablefmt="fancy_grid"))
                    break
                return

            #after all the conditions, now print out the datatable we are left with.
            print(tabulate(datatable, headers="firstrow", tablefmt="fancy_grid"))
    
    except Exception as e:
        sys.exit(f"Unable to open file!: {e}.")
