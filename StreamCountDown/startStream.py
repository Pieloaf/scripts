from multiprocessing import Process
from time import sleep
from os import path, getcwd, remove, stat, listdir
from pathlib import Path
import getopt
import sys

from menu import Menu
import config

def write(msg, file):
	file = file+'.txt'
	ofile = open(file, 'w', encoding='utf-8')
	ofile.write(msg)
	ofile.close()

def timer(m):
    s = 0
    while m >= 0 and s >= 0:
        sleep(1)
        s -= 1
        
        if s < 0 and m != 0:
            m -= 1
            s = 59

        msg = str(m).zfill(2)+':'+str(s).zfill(2)
        print (msg, end='\r')
        write(msg, 'time')

    print('Time to start')
    while True:
        msg = (['00:00', '    '])
        for i in msg:
            write(i, 'time')
            sleep(1)
    
def dotText(text, file):
    while True:
        sleep(1)
        msg = text
        write(msg, file)
        
        for i in range(3):
            sleep(1)
            msg += "."
            write(msg, file)

def loading(m, l):
    dly = (m*60)/l
    msg = ''
    for i in range(l):
        msg += '░'
    write(msg, 'loading')
    msglst = list(msg)
    
    for i in range(l):
        sleep(dly)
        msglst[i]='█'
        write(''.join(msglst), 'loading')

def percentage(m):
    per_inc = (m*60)/100
    per_comp = 0
    
    while per_comp < 100:
        sleep(per_inc)
        per_comp += 1
        write(str(round(per_comp)).zfill(2)+'%', "percentage")

    per_comp = 100

def noArgs():
    cwd = getcwd()
    if (not path.isfile(path.join(cwd,'default.config'))) or (stat('default.config').st_size == 0):
        config.invalidDefault(cwd)
    else:
        defaultConfig = open('default.config', 'r')
        confName = defaultConfig.readlines()[0]
        defaultConfig.close()
        if not path.isfile(path.join(cwd,(confName+'.toml'))):
            print('File not found')
            config.invalidDefault(cwd)
        else:
            procs = config.loadConfig(confName)
            for proc in procs:
                proc.start()

def main():
    usage = '==Usage==\npython startStream.py [OPTION...] [FILE...]\n\nNo arguments \t\t\tUses default config file\n-d --default\t<fName.toml>\tSets fName.toml as default config\n-c --config\t<fName.toml>\tUses fName.toml as config\n-n --new\t\t\tCreates new config file\n-h --help\t\t\tDisplays this help message'
    fileNotFound = 'Error: File Not Found'

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'd:c:hn',['default=','config=','help','new'])
    except getopt.GetoptError:
        print(usage)
        return

    if len(argv) == 0:
        noArgs()
    elif len(argv) > 2:
        print(usage)
    else:
        for opt, arg in opts:
            if opt in ("-d","--default"):
                if path.isfile(path.join(getcwd(),arg)):
                    config.setDefault(arg[:-5])
                    return
                else:
                    print(fileNotFound)
                    config.invalidDefault(getcwd())
                    return
            
            elif opt in ['-c','--config']:
                if not path.isfile(path.join(getcwd(),arg)):
                    print(fileNotFound)
                    print('Please try again with a valid config file. Run with -h for more details')
                    return
                else:
                    procs = config.loadConfig(arg[:-5])
                    for proc in procs:
                        proc.start()

            elif opt in ['-h','--help']:
                print(usage)
                return

            elif opt in ['-n','--new']:
                config.newConfig()
                return
            else:
                print('nope')

if __name__ == '__main__':
    main()