from tabulate import tabulate

def format_table(datatable):
    return tabulate(datatable, headers="firstrow", tablefmt="fancy_grid")
