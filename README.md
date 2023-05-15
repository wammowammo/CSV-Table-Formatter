# Table-Formatter
Python command line program which reads a file containing data in csv format, outputs to terminal a well formatted table

## Table of Contents
1. [Overview](#overview)
   * [Description](#description)
   * [Modules](#modules)
2. [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Installing Required Libraries](#installing-required-libraries)
3. [Running the Code](#running-the-code)
   * [Command-line Options](#command-line-options)
4. [Usage Examples](#usage-examples)
5. [Directory](#directory)
   * [Included Files](included-files)
   * [License](#license)

## Overview
### Description
CSV Table Viewer is a command-line application that formats and prints a CSV file provided by the user. The program gives the user ability to customize how they want the data from the CSV file to be printed out by adding into the commandline how they want their data to be printed out. See [Running the Code](#running-the-code)

With its simple and intuitive command-line interface, the CSV Table Viewer program provides a convenient tool for users who need to quickly view and manipulate data stored in CSV files.

### Modules
The application has 4 main modules:

* `showTable.py` - This module is the main script that is called in the command-line.

* `cmdline_parser.py` - This module parses and stores the command-line arguments to be used later.

* `data_reader.py` - This module cleans the data to remove it of any incomplete or unreadable data and stores it into a 2D list.

* `tblformatter.py` - This module further formats the table based on the arguments that are provided by the user and then prints the 2D list into a visually appealing table to be viewed by the user.

## Getting Started
Follow these steps to set up and run the CSV Table Viewer program:

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.6 or higher
- `csv` library
- `tabulate` library

### Installing Required Libraries

To install the required libraries, open a terminal and run the following command:

```bash
pip install csv tabulate
```

## Running the Code

To run the application, open a terminal and use ls and cd to navigate to the directory containing the showTable files. Then, run the following command:

```bash
python3 showTable.py [options] <data_file>
```

where `[options]` are optional command-line arguments and `data_file` is the path to the input CSV file.

### Command-line Options

- `-s <character>`: specifies the separator of the fields (default is ',')
- `-l`: outputs only the list of column headers
- `-o <column>`: includes only the specified column; can be used repeatedly to include more columns; order matters; (default: lists all columns)
- `-u <column>`: sort the table by ordering the specified column in ascending order (default: no sort)
- `-d <column>`: sort the table by ordering the specified column in descending order (default: no sort)
- `-m <string>`: lists only the rows having at least one element containing the string; multiple appearances are joined by
- `-n <number>`: displays only the first specified number of rows of the table

## Usage Examples

1. Display the table with default settings:
```bash
python3 showTable.py example.csv
```

2. Use a different column separator:
```bash
python3 showTable.py -s "|" example.csv
```

3. Display only column headers:
```bash
python3 showTable.py -l example.csv
```

4. Display the two following columns:
```bash
python3 showTable.py -o Phone Name example.csv 
```

5. Sort rows by the Name column in ascending order:
```bash
python3 showTable.py -u Name example.csv
```

6. Sort rows by the Name column in descending order:
```bash
python3 showTable.py -d Name example.csv
```

7. Filter rows based on the string "on":
```bash
python3 showTable.py -m "on" example.csv
```

8. Display the first 10 rows of the table:
```bash
python3 showTable.py -n 10 example.csv
```

## Directory

### Included Files
To see a test example containing a curated CSV file data, view: 
* ```testfile.csv```

For information regarding the API used by the CSV Table Viewer program modules, view:
* ```api_description.md```

For information regarding the dependencies used in the CSV Table Viewer program, view:
* ```dependencies.md```

For information regarding the data printed by the CSV Table Viewer program using the example data, view:
* ```example_output.md```

### License
[MIT](https://choosealicense.com/licenses/mit/)
