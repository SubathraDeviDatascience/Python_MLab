import sys
def cli_parser(command):
    switcher={
        'stop':'Stopping the program...',
        'restart':'Restarting the program...',
        'start':'Starting the program...'
    }
    return switcher.get(command,None)
if len(sys.argv)>1:
    print(cli_parser(sys.argv[1]))
else:
    print("No commandline provided")