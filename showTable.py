import argparse
import sys
import string
import csv
from tblformatter import format_table

from cmdline_parser import cmdlineargs
import pandas as pd


def main(args):

    if args.s is None:
        args.s = ","
    if(type(args.s)!=str):
        sys.exit("separator must be a string")
    if(len(args.s)!=1):
        sys.exit("separator must be 1 character long")
    if(args.s not in string.printable):
        sys.exit("separator must be printable")
    
    if(len(args.files)==1):
        file = args.files[0]
    else:
        sys.exit("wrong number of files provided")

    # Open the CSV file
    with open(file, 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)

        # Read and process each row in the CSV file
        datatable = []
        for row in reader:
            datatable+=[row]
        print(format_table(datatable))

if __name__ == '__main__':
    args = cmdlineargs()
    main(args)