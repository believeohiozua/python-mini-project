import pandas as pd


class DataFrameContextManager:
    
    def __init__(self, filename, mode ):
        self.df = pd.read_csv(filename, sep=mode)
        self.columns = list(self.df.columns.values)

    def __enter__(self):
        return self.df

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.df.drop([c for c in self.columns], axis=1, inplace=True)

class SpreadSheetIterator(DataFrameContextManager):
    def __init__(self,file_path, mode):       
        self.file_path = file_path
        self.mode = mode

    def sheet_iterator(self):
        try:            
            data = DataFrameContextManager(self.file_path, self.mode) 
            row_no = 0
            for index, row,  in data.df.iterrows():
                row_no += 1
                print(f'At row {row_no} column {data.columns} conatins {row}\n')              
            return data.df               
        except Exception as e:
            print('Error ! :', e)


class PrintCompleteContent(DataFrameContextManager):
    def __init__(self,file_path, mode):       
        self.file_path = file_path
        self.mode = mode

    def print_contents(self):
        try:            
            data = DataFrameContextManager(self.file_path, self.mode)  
            print(data.df)         
            return data.df               
        except Exception as e:
            print('Error ! :', e)


class PrintFirstTwoLines(DataFrameContextManager):
    def __init__(self,file_path, mode):       
        self.file_path = file_path
        self.mode = mode

    def row_printer(self):
        try:            
            data = DataFrameContextManager(self.file_path, self.mode)  
            print(data.df.iloc[:2])         
            return data.df.iloc[:2]              
        except Exception as e:
            print('Error ! :', e)



class PrintLastTwoLines(DataFrameContextManager):
    def __init__(self,file_path, mode):       
        self.file_path = file_path
        self.mode = mode

    def row_printer(self):
        try:            
            data = DataFrameContextManager(self.file_path, self.mode)  
            print(data.df.iloc[-2:])         
            return data.df.iloc[-2:]              
        except Exception as e:
            print('Error ! :', e)


# checker = DataFrameContextManager('../files/sample.tsv', '\t')
# print(checker.df)
# checker.df