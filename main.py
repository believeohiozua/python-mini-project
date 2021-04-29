import os
import sys
from src.ReadBytesFromFile import *
from src.ProcessSpreadSheet import *



def main():
    arg = sys.argv
    action = None
    file_path = None
    try:
        action = arg[1]
        file_path = arg[2]
    except Exception as e:
         print(
            'To test read bytes\n',
            'python main.py read-iterate path-to-file \n',
            'python main.py read-read path-to-file\n',
            'python main.py read-first2 path-to-file\n',
            'python main.py read-last2 path-to-file\n',
            '\nTo test process bytes\n',
            'python main.py process-iterate path-to-file \n',
            'python main.py process-read path-to-file\n',
            'python main.py process-first2 path-to-file\n',
            'python main.py process-last2 path-to-file\n',
            '\nTo run test\n'
            'python main.py run test\n',
)
    try:    
        if action == 'read-iterate':
            if file_path:
                line_finder = ObjectIterator(file_path , 'r')
                return line_finder.line_reader()
        elif action == 'read-complete':
            if file_path:
                file_reader= CompleteContentReader(file_path , 'r')
                return file_reader.filer_reader()
        elif action == 'read-first2':
            if file_path:
                file_reader= ReadFirstTwoLines(file_path , 'r')
                return file_reader.first_lines_reader()
        elif action == 'read-last2':
            if file_path:
                file_reader= ReadLastTwoLines(file_path , 'r')
                return file_reader.last_lines_reader()

        elif action == 'process-iterate':
            if file_path and file_path[-3:] == 'csv':                
                line_finder = SpreadSheetIterator(file_path)
                return line_finder.sheet_iterator()
            elif file_path and file_path[-3:] == 'tsv':  
                line_finder = SpreadSheetIterator(file_path, '\t')
                return line_finder.sheet_iterator()
                
        elif action == 'process-complete':
            if file_path and file_path[-3:] == 'csv':                
                file_reader= PrintCompleteContent(file_path)
                return file_reader.print_contents()
            elif file_path and file_path[-3:] == 'tsv':  
                file_reader= PrintCompleteContent(file_path , '\t')
                return file_reader.print_contents()                
        
                
        elif action == 'process-first2':
            if file_path and file_path[-3:] == 'csv':                
                file_reader= PrintFirstTwoLines(file_path)
                return file_reader.row_printer()
            elif file_path and file_path[-3:] == 'tsv':  
                file_reader= PrintFirstTwoLines(file_path , '\t')
                return file_reader.row_printer()        
                
        elif action == 'process-last2':
            if file_path and file_path[-3:] == 'csv':                
                file_reader= PrintLastTwoLines(file_path)
                return file_reader.row_printer()
            elif file_path and file_path[-3:] == 'tsv':  
                file_reader= PrintLastTwoLines(file_path , '\t')
                return file_reader.row_printer()
        elif action == 'run':
            os.system('cd src && python3 test_initial.py')
        else:
            print(f'please refer to the Read.md file for how to run this program. \n Thanks')

    except Exception as e:
        print(f'Error! : {e}')
    
            

if __name__ == '__main__':
    main()




# to test read bytes
# python3 main.py read-iterate path-to-file 
# python3 main.py read-read path-to-file
# python3 main.py read-first2 path-to-file
# python3 main.py read-last2 path-to-file

# to test process bytes
# python3 main.py process-iterate path-to-file 
# python3 main.py process-read path-to-file
# python3 main.py process-first2 path-to-file
# python3 main.py process-last2 path-to-file


# to run test
# python3 main.py run test