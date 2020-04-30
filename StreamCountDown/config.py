from multiprocessing import Process
import toml
import startStream as sStream
from menu import Menu
import os
from pprint import pprint

global defaultPath
defaultPath = os.path.join(os.getcwd(),'default.config')


def loadConfig(file):
    fName = (file+'.toml')
    config = toml.load(fName)
    procs = []
    m = config['timeLen']

    if config['time']['active'] == True:
        procs.append(Process(target = sStream.timer, args=(m,)))

    if config['bar']['active'] == True:
        procs.append(Process(target = sStream.loading, args=(m,config['bar']['barLen'],)))

    if config['percent']['active'] == True:
        procs.append(Process(target= sStream.percentage, args=(m,)))

    if config['text']['active'] == True:
        for i in range(config['text']['numItems']):
            procs.append(Process(target=sStream.dotText, args=(config['text']['textLi'][i], 'text'+str(i))))

    return procs    

def setDefault(confN):
    file = open(defaultPath, 'w')
    file.write(confN)
    file.close()

def saveConf(confList):
    confN = input('Save As: ')
    tomlWriter(confList, confN)

    print("Config Saved!")
    if not os.path.isfile(defaultPath):
        open('default.config','w').close()
        setDefault(confN)
    else:
        while True:
            defConf = input("Set as Defualt?(y/n): ")
            if defConf == 'y':
                setDefault(confN)
                break
            elif defConf == 'n':
                break
            else:
                print("Invalid Option")

def editConf(confList):
    print('WIP')

def newConfig(): ##WIP
    default = [5,True,True,20,True,True,1,["Starting Soon"]]
    newConfLi = default
    inputChoice = 0
    print("===New Configuration Setup===")
    def cancel():
        print('Cancelling...')

    def viewConf(confDic):
        pprint(confDic)
    while inputChoice != 4:
        
        edit = Menu(['View Current Config','Edit Config','Save Config','Cancel'],[viewConf, editConf, saveConf, cancel],[[newConfLi],[newConfLi],[newConfLi],[]])
        inputChoice = int(input(edit))
        edit.choice(inputChoice)

def tomlWriter(confVals,fName):

    file = open(fName+'.toml', 'w')
    newConf = dict()
    newConf = {
        'timeLen': confVals[0]}
    newConf['time'] = {
        'active': confVals[1]}
    newConf['bar'] = {
        'active': confVals[2], 
        'barLen': confVals[3]}
    newConf['percent'] = {
        'active': confVals[4]}
    newConf['text'] = {
        'active': confVals[5],
        'numItems': confVals[6],
        'textLi': confVals[7]}

    toml.dump(newConf, file)
    file.close()

def init(): ##WIP
    cwd = os.getcwd()
    confs = []
    for file in os.listdir(cwd):
        if file[-5:] == '.toml':
            confs.append(file)
    if len(confs) < 1:
        newConfig()
        set
    elif len(confs) == 1:
        loadConfig('123')
    else:
        print(confs)