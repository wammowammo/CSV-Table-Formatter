import argparse
import sys

#parse through the commandline arguments
def cmdlineargs():
    parser = argparse.ArgumentParser()

    #specify the separator
    parser.add_argument('-s', type=str, help='Choose the separator! Default will be ","')
    
    #only display header row
    parser.add_argument('-l', action='store_true', help='Only display column names')
    
    #specify which columns to display
    parser.add_argument('-o', nargs ='+', type=str, help='Choose which columns to display')
    
    #sort the table in ascending order based off a column
    parser.add_argument('-u', type=str, help='Sort the table in ascending order based off a column')
    
    #sort the table in descending order based off a specified column
    parser.add_argument('-d', type=str, help='Sort the table in descending order based off a column')
    
    #Only list rows that contain a particular value
    parser.add_argument('-m', type=str, help='Only list the rows that contain a given string')
    
    #Only display the first n number of rows
    parser.add_argument('-n', type=int, help='Displays only the first specified number of rows')
    
    
    parser.add_argument("files", type=str, nargs='+', help="Path to input file")
    try:
        args = parser.parse_args()
        return args
    except Exception as e:
        sys.exit(f"Error: Unable to parse arguments: {e}")