from multiprocessing import Process
import toml
import os
import startStream as sStream
from menu import Menu

global defaultPath
defaultPath = os.path.join(os.getcwd(),'default.config')

def back():
    return

def yesNo(text):
    hold = 0
    while hold == 0:
        choice = input(text+' (y/n): ')
        if (choice == 'y') or (choice == 'Y'):
            return True
        elif (choice == 'n') or (choice == 'N'):
            return False
        else:
            print('Invalid input. Please try again.')

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
    if (not os.path.isfile(defaultPath)) or (os.stat('default.config').st_size == 0):
        open('default.config','w').close()
        setDefault(confN)
    else:
        while True:
            defConf = yesNo('Set as Defualt?')
            if defConf == True:
                setDefault(confN)
                break
            elif defConf == False:
                break
            else:
                print("Invalid Option")

def duration(toChange):
    while True:
        try:
            toChange = int(input('Timer Duration (mins): '))
            break
        except ValueError:
            print('Please Enter an Interger')

def cdm(toChange):
    print('\nCount Down Module:')
    toChange = yesNo('Active')

def ldm_menu(confList):
    menu = Menu(['Activate', 'Set Bar Length', 'Back'], [lbm_activate, lbm_length, back],[[confList[2]], [confList[3]],[]])

    while True:
        try:
            inputChoice = int(input('\n'+str(menu)))
        except ValueError:
            print('Please Enter an Interger')
        except IndexError:
            print('Please Enter a Valid Option')
        menu.choice(inputChoice)
        if (inputChoice == 3):
            break

def lbm_activate(toChange):
    print('\nLoading Bar Module:')
    toChange = yesNo('Active')

def lbm_length(toChange):
    while True:
        try:
            toChange = int(input('Loading Bar Length: '))
            break
        except ValueError:
            print('Please Enter an Interger')

def pcm(toChange):
    print('\nPercenatge Module:')
    toChange = yesNo('Active')

def txtm_menu(confList):
    menu = Menu(['Activate', 'Set Items', 'Back'], [txtm_activate, txtm_items, back],[[confList[5]], [confList], []])

    while True:
        try:
            inputChoice = int(input('\n'+str(menu)))
        except ValueError:
            print('Please Enter an Interger')
        except IndexError:
            print('Please Enter a Valid Option')
        menu.choice(inputChoice)
        if (inputChoice == 3):
            break

def txtm_activate(toChange):
    print('\nText Module:')
    toChange = yesNo('Active')

def txtm_items(confList):
    confList[7] = []
    while True:
        try:
            confList[6] = int(input('Number of Text Items: '))
            break
        except ValueError:
            print('Please Enter an Interger')
        except IndexError:
            print('Please Enter a Valid Option')       

    for i in range(confList[6]):
        confList[7].append(input('Message '+str(i)+': '))
    else:
        pass

def editConf(confList):
    
    changes = Menu(['Duration', 'Count Down Module', 'Loading Bar Module', 'Percentage Module', 'Text Modules', 'Exit'],[duration, cdm, ldm_menu, pcm, txtm_menu, cancel],[[confList[0]], [confList[1]], [confList], [confList[4]], [confList], []])

    while True:
        try:
            inputChoice = int(input('\n'+str(changes)))
        except ValueError:
            print('Please Enter an Interger')
        except IndexError:
            print('Please Enter a Valid Option')
        changes.choice(inputChoice)
        if (inputChoice == 6):
            break

def viewConf(confVals):
    print('\n==Current Configuration==')
    print('\nDuration: '+str(confVals[0])+'\n\nCount Down Module:\nActive: '+str(confVals[1])+'\n\nLoading Bar Module:\nActive: '+str(confVals[2])+'\nLength of Bar: '+str(confVals[3])+'\n\nPercentage Module:\nActive: '+str(confVals[4])+'\n\nText Modules:\nActive: '+str(confVals[5])+'\nText Items: '+str(confVals[6])+'\nMessages:\n\t'+('\n\t'.join(confVals[7])))

def cancel():
    print('Cancelling...')
    return

def newConfig():
    default = [5,True,True,20,True,True,1,["Starting Soon","Loading"]]
    newConfLi = default
    inputChoice = 0
    print("===New Configuration Setup===")

    while (inputChoice != 3) and (inputChoice != 4):
        edit = Menu(['View Current Config','Edit Config','Save Config','Cancel'],[viewConf, editConf, saveConf, cancel],[[newConfLi],[newConfLi],[newConfLi],[]])
        
        while True:
            try:
                inputChoice = int(input('\n'+str(edit)))
                break
            except ValueError:
                print('Please Enter an Interger')
            except IndexError:
                print('Please Enter a Valid Option')

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

def invalidDefault(cwd):
    tomls = []
    for file in os.listdir(cwd):
        if file[-4:] == 'toml':
            tomls.append(file)
    if len(tomls) == 0:
        print('No config files found. Creating new config...\n')
        newConfig()
    else:
        print("Config files found!")
        print("Choose a config to set as default:")
        for file in tomls:
            print(str((tomls.index(file)+1))+'. '+file[:-5])

        while True:
            try:
                setDefault(tomls[int(input())-1][:-5])
                break
            except ValueError:
                print('Please Enter an Interger')
            except IndexError:
                print('Please Enter a Valid Option')