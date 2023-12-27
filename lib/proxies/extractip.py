import re
from proxy import proxy
from prettytable import PrettyTable


def extract():

    # Sample string containing multiple IP addresses and ports
    ip_ports = proxy()

    # Regular expression pattern to match IP address and port pairs
    pattern = r"(\d+\.\d+\.\d+\.\d+):(\d+)"

    # Finding all IP address and port matches
    matches = re.findall(pattern, ip_ports)

    # Creating a PrettyTable object
    table = PrettyTable()
    table.field_names = ["IP Address", "Port"]

    # Adding IP address and port pairs to the table
    for ip, port in matches:
        table.add_row([ip, port])

    # Printing the table
    return table

print(extract())
