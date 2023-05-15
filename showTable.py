import sys
import string
import tblformatter
import os

from cmdline_parser import cmdlineargs

#main function that is gets run
def main():
    args = cmdlineargs()
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
    if not os.path.exists(file):
        sys.exit("The file '{file}' does not exist.")
    if os.path.getsize(file) == 0:
        sys.exit("Error: The file '{file}' is empty.")

    tblformatter.format_table(file, args)


#run main IF this module is being called as the main function.
if __name__ == '__main__':
    main()