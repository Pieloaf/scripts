from multiprocessing import Process
from time import sleep
import sys
import toml
from menu import Menu
import config
from os import path

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

if __name__ == '__main__':
    #if path,isf'default.config'
    #    os.path.r
    #except NotA
    config.newConfig()
    print("--===-=-=-=-=-==-")
    procs = config.loadConfig('123')
    for proc in procs:
        proc.start()