import sys
from core import importer

def main():
    print("Hello World!")

if __name__ == "__main__":
    #print(sys.argv[1])
    if sys.argv[1] == 'import_mov':
        if '-h' in sys.argv[1:]:
            print('''
            import_mov file_path year
            import movemnts files to the system
            ''')
        else:
            imp = importer.importer()
            #print(sys.argv[2],sys.argv[3])
            imp.read_file_ETrade(sys.argv[2],sys.argv[3])
    