


class saveCSV:
    def __init__(self,filepath:str,justreading:bool = False) -> None:
        import csv
        self.filePATH = filepath
        if self.filePATH.endswith('.csv'):
            self.filePATH += '.csv'
        if not justreading:
            self.file = open(filepath,mode='w',newline='')
            self.writer = csv.writer(self.file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        else:
            self.file = open(filepath,mode='r')
            self.reader = csv.reader(self.file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            
    def add_row(self,row):
        self.writer.writerow(row)
    
    def add_rows(self,rows):
        self.writer.writerows(rows)
    
    def read_row(self,rowcount):
        rows = [row for row in self.reader]
        rowcount -= 1 
        if rowcount > len(rows):
            print('Satır üzerinde herhangi bir bilgi bulunmamakta.')
            return None
        return rows[rowcount]
            
        
    def read_rows(self):
        return [row for row in self.reader]     
    
    def close(self):
        self.file.close()
