import os,sys


def proxy():

    filename = "proxy.txt" 
    current_directory = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(current_directory, filename) 

    with open(file_path, "r") as file: 
        payload = file.read()
        rows = payload.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows) #* 
        return sorted_payload

# print(proxy())