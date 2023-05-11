import argparse
import sys

from cmdline_parser import cmdlineargs
import pandas as pd


def main(args):

    if args.separator is None:
        args.separator = ","
    if(type(args.separator)!=str):
        sys.exit("separator must be a string")
    if(len(args.separator)!=1):
        sys.exit("separator must be 1 character long")
    if(args.separator not in args.separator.printable):
        sys.exit("separator must be printable")

    file = args.file[0]


if __name__ == '__main__':
    args = cmdlineargs();