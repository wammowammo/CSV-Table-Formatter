# CSV Table Viewer Program

Below are brief documentation of each fule used in the CSV Table Viewer program.  In general, the CSV Table Viewer program **consists** of:
* `showTable.py`
* `cmd_parser.py`
* `data_reader.py`
* `table_formatter.py`


## `showTable.py`
The main module of the CSV Table Viewer program which is responsible for calling the other modules and executing the program's main logic. This module takes command-line arguments from the user, which include the path to the CSV file, the columns to display, and any filters to apply to the data.

* `argv` (input parameter): Command-line arguments from the user, including the path to the CSV file, the columns to display, and any filters to apply to the data.

This API retrives data from:
* the object that contains the values of the parsed arguments based on the input arguments inputted by the user via`cmd_parser.py`,
* the Pandas DataFrame created by reading the CSV file via `data_reader.py`,
* the formatted DataFrame as a human-readable ASCII table via `table_formatter.py` to which is printed to the console for the user to view in this main file

## `cmd_parser.py`
A module that is used to parse the command-line arguments passed to the program. It takes the argv list from showTable.py and parses it to extract the path to the CSV file, the list of columns to display, and any filters to apply to the data.

* `argv` (input parameter): Command-line arguments from the user, including the path to the CSV file, the columns to display, and any filters to apply to the data.
* `get_file_path()` (output parameter): Returns the path to the CSV file as a string.
* `get_columns()` (output parameter): Returns a list of columns to display in the table.
* `get_filters()` (output parameter): Returns a list of filters to apply to the data.

This API retrieves the filename, delimiter, header, sort, ascending, and filter data from the command-line arguments inputted by the user.

## `data_reader.py`
A module that is responsible for reading the data from the CSV file and converting it into a pandas DataFrame. It takes the file path from cmd_parser.py and uses the pandas library to read the CSV file and convert it into a DataFrame.

* `file_path` (input parameter): The path to the CSV file as a string.
* `read_data()` (output parameter): Returns a pandas DataFrame object containing the data from the CSV file.

This API takes in a file path as input and returns a pandas DataFrame object by reading the data from the CSV file and returning it in a format that can be easily used by the other modules.

## `table_formatter.py`
A module that is responsible for formatting the data from the pandas DataFrame and displaying it to the user. It takes the DataFrame from data_reader.py and uses the tabulate library to format the data into a human-readable table.

* `data` (input parameter): The pandas DataFrame object containing the data from the CSV file.
* `columns` (input parameter): A list of columns to display in the table.
* `filters` (input parameter): A list of filters to apply to the data.
* `format_data()` (output parameter): Returns a formatted string that represents the data in the DataFrame, including the specified columns and filters.

This API is focused on taking structured data and presenting it in a visually appealing and easy-to-read format for display in a terminal/console, as well as for exporting data to a file or other output medium.