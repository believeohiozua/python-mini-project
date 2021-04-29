class ContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


class ObjectIterator(ContextManager):
    def __init__(self,file_path, mode):       
        self.file_path = file_path
        self.mode = mode

    def line_reader(self):
        try:            
            with ContextManager(self.file_path, self.mode) as filehandle:
                current_line = 0
                for line in filehandle:
                    current_line += 1
                    print(f'on line {current_line} is : {line}')
        except Exception as e:
            print('Error ! :', e)


class CompleteContentReader(ContextManager):
    def __init__(self,file_path, mode):             
        self.file_path = file_path
        self.mode = mode

    def filer_reader(self):
        try:
            with ContextManager(self.file_path, self.mode)  as filehandle:
                filecontent = filehandle.read()
                print(filecontent)
        except Exception as e:
            print('Error !: ', e)


class ReadFirstTwoLines(ContextManager):
    def __init__(self,file_path, mode):             
        self.file_path = file_path
        self.mode = mode

    def first_lines_reader(self):
        try:
            with ContextManager(self.file_path, self.mode) as filehandle:
                line1, line2 = next(filehandle), next(filehandle)
                line_count = 0
                for line in [line1, line2]:
                    line_count += 1
                    print(f'on line {line_count} is : {line}')
        except Exception as e:
            print('Error! : ', e)


class ReadLastTwoLines(ContextManager):
    def __init__(self,file_path, mode):             
        self.file_path = file_path
        self.mode = mode

    def last_lines_reader(self):
        try:
            with ContextManager(self.file_path, self.mode) as f:
                data = f.readlines()
                tail = ''.join(data[-2:])
            print(f'\nthe last two lines in {self.file_path} are : \n{tail}\n')
        except Exception as e:
            print('Error! : ', e)


# a = ObjectIterator('../files/sample.tsv', 'r')
# a.line_reader()