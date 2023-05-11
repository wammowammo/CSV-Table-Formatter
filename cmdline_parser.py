import argparse

def cmdlineargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--separator', type=str, help='Choose the separator! Default will be ","')
    parser.add_argument('-l', '--list', action='store_true', help='Only display column names')
    

    return parser.parse_args()
