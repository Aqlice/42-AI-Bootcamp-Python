import sys
import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if not all((isinstance(filename, str), isinstance(sep, str), \
            isinstance(header, bool), isinstance(skip_top, int), isinstance(skip_bottom, int))):
            sys.exit("wrong arguments")
        self.filename = filename
        self.file = None
        self.data = []
        self.head = None
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            reader = csv.reader(self.file, delimiter=self.sep)
        except:
            return None
        
        for i, line in enumerate(reader):
            for elem in line:
                if len(elem) == 0:
                    return None
            if i == 0 and self.header == True:
                self.head = line
            elif i >= self.skip_top and (i < self.skip_bottom or self.skip_bottom == 0):
                self.data.append(line)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file is not None:
            self.file.close()
    
    def getdata(self):
        return self.data
    
    def getheader(self):
        return self.head

if __name__ == "__main__":
    with CsvReader("TEST.csv", sep=';', header=True, skip_top=15) as file:
        if file is None:
            print("File not found or is corrupted")
            exit()
        print(f'Header:\n{file.head}')
        print(f'Data:')
        for data in file.getdata():
            print(f'{data}')