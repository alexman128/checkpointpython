import json
import csv

class CSVFile():
    '''
    This class handle a csv file using following parameters:
    file_dir:
    '''
    def __init__(self, file_dir:str, content:dict, mode:str = 'a'):
        self.file_dir = file_dir
        self.content = content
        self.mode = mode

    def write_content(self):
        with open(self.file_dir,self.mode) as my_file:
            writer = csv.writer(my_file, quoting=csv.QUOTE_ALL)
            #writer.writeheader()
            writer.writerow(self.content)    
