import argparse

def cmdlineargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, help='Choose the separator! Default will be ","')
    parser.add_argument('-l', action='store_true', help='Only display column names')
    parser.add_argument('-o', nargs = '+', type=int, help='Choose which columns to display')
    parser.add_argument('-u', type=str, help='Sort the table in ascending order based off a column')
    parser.add_argument('-d', type=str, help='Sort the table in descending order based off a column')
    parser.add_argument('-m', type=str, help='Only list the rows that contain a given string')
    parser.add_argument('-n', type=int, help='Displays only the first specified number of rows')
    parser.add_argument("files", type=str, nargs='+', help="Path to input file")

    return parser.parse_args()
