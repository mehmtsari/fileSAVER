
class saveTXT:
    def __init__(self,filename:str,mode:str) -> None:
        """filename : Must be 'filename.txt'
        mode ; 
            'w' : Open new one
            'a' : if have, read. dont have, create
            'r' : just read
        """
        self.file_name = filename
        self.file = open(filename,mode)
        
    def add_row(self,Text):
        self.file.write(Text)
        self.file.write('\n')
        
    def add_rows(self, RowList:list):
        for item in RowList:
            self.file.write(item)
            self.file.write('\n')
    
    def read_all(self):
        return self.file.read()
    
    def read_lines(self):
        return self.file.readlines()

    def saveTXT(self):
        """Closing the TXT file
        """
        self.file.close()




