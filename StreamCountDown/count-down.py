from time import sleep
from multiprocessing import Process
import sys

def write(msg, filen):
	file = filen+'.txt'
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
        print(msg)       
        write(msg, 'time')

    print('Time to start')
    while True:
        msg = (['00:00', '    '])
        for i in msg:
            write(i, 'time')
            sleep(1)
    
def startSoon():
    while True:
        sleep(1)
        msg = "Starting Soon"
        write(msg, 'starting_soon')
        
        for i in range(3):
            sleep(1)
            msg += "."
            write(msg, 'starting_soon')

def loading(m):
    dly = (m*60)/20
    msg = ''
    for i in range(20):
        msg += '░'
    write(msg, 'loading')
    msglst = list(msg)
    
    for i in range(20):
        sleep(dly)
        msglst[i]='█'
        write(''.join(msglst), 'loading')


if __name__ == '__main__':
    mins = int(input("mins:\n"))
    p1 = Process(target = startSoon)
    p2 = Process(target = timer, args=(mins,))
    p3 = Process(target = loading, args=(mins,))
    p1.start()
    p2.start()
    p3.start()
