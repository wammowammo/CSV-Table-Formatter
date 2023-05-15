import argparse
import sys
import re
import os

#parse through the commandline arguments
def cmdlineargs():
    #this block of code enables '-o' to be able to be put either before OR
    #after the csv file is typed into the commandline.
    argv = sys.argv[1:]
    if '-o' in argv:
        o_index = argv.index('-o')
        for i in range(o_index + 1, len(argv)):
            if re.match(r'.*\.csv$', argv[i]):
                argv.insert(i, '--') 
                break

    def file_path(path):
        if os.path.isfile(path):
            return path
        else:
            raise argparse.ArgumentTypeError(f"{path} is not a valid file path")

    def positive_int(n):
        n = int(n)
        if n > 0:
            return n
        else:
            raise argparse.ArgumentTypeError(f"{n} is not a positive integer")

    parser = argparse.ArgumentParser()

    # specify the separator
    parser.add_argument('-s', type=str, help='Choose the separator! Default will be ","')
    
    # only display header row
    parser.add_argument('-l', action='store_true', help='Only display column names')
    
    # specify which columns to display
    parser.add_argument('-o', nargs ='+', type=str, help='Choose which columns to display')
    
    # sort the table in ascending order based off a column
    parser.add_argument('-u', type=str, help='Sort the table in ascending order based off a column')
    
    # sort the table in descending order based off a specified column
    parser.add_argument('-d', type=str, help='Sort the table in descending order based off a column')
    
    # Only list rows that contain a particular value
    parser.add_argument('-m', type=str, help='Only list the rows that contain a given string')
    
    # Only display the first n number of rows
    parser.add_argument('-n', type=positive_int, help='Displays only the first specified number of rows')
    
    # take in the file that the user provides.
    parser.add_argument("files", type=file_path, nargs='+', help="Path to input file")

    # try to parse the arguments, exit otherwise
    try:
        args = parser.parse_args(argv)  # Pass the pre-processed argument list
        return args
    except Exception as e:
        sys.exit(f"Error: Unable to parse arguments: {e}")
