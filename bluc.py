import sys
from interpreter import run_file

def main():
    if len(sys.argv) < 3:
        print('Bluucode CLI')
        print('Usage: ')
        print('bluc run <file.bluc>')
        return

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == 'run':
        run_file(filename)
    else:
        print(f'''Unknown Command: '{command}' ''')

if __name__ == '__main__':
    main()