import os
from menu import Menu


def projectDir():
    global Dir, DirInc, DirSrc

    #path to project directory
    Dir = input("Project Directory: ")
    DirInc = Dir + "/include"
    DirSrc = Dir + "/src"

    #creating neccessary folders
    if (os.path.exists(DirInc) and os.path.exists(DirSrc)):
        pass
    elif (os.path.exists(Dir)): 
        os.mkdir(DirInc)
        os.mkdir(DirSrc)
    else:
        cont = input("Specified directory does not exist. Do you want to create it?[y/n]")
        if (cont == "y"):
            os.makedirs(Dir)
            os.mkdir(DirInc)
            os.mkdir(DirSrc)
        elif (cont == "n"):
            projectDir()
    return

#main menu
def mainM():
    global main
    
    main = Menu(["Add Class","Quit"], [newClass, quit])
    
    print(main)
    x = input()
    main.choice(x)
    return

#new class
def newClass():
    global nClass, flag,  name, public, private, protected, inher, setrgetr
    flag = 0
    public = [ ]
    private = [ ]
    protected = [ ]
    setrgetr = [ ]
    inher = False

    nClass = Menu(["Add Data Member","Inheritance","Done","Cancel"],[newDataMem,relo,writeClass,mainM])    
    
    #taking class name 
    name = input("Class Name: ")
   
    while(flag==0):
        print(nClass)
        x = int(input())

        if (x == 2): #inheritance flag
            inher = True

        nClass.choice(x)    
    return

def quit():
    exit()
    return

def writeClass():

    #writing to header file
    
    #create setters and getters?
    setterget = input("Create Setters and Getters?[y/n]\n")

    if (setterget == "y"):
        setget()
    else:
        pass
    
    #writing file header
    f=open(DirInc+'/'+name+'.h',"w+")
    f.write("#ifndef "+name.upper()+"_H\n")
    f.write("#define "+name.upper()+"_H\n")

    #class name and inheritance
    if (inher==True):
        f.write("class "+name+parent+"\n")
    else:
        f.write("class "+name+"\n")
    f.write("{\n")
    
    #writing data members
    f.write("   public:\n")
    f.write("        "+name+"();\n        virtual ~"+name+"();\n")

    for mem in public:
    	f.write("        "+mem+";\n")
    
    for mem in setrgetr:
        f.write("        "+mem+"\n")

    f.write("   protected:\n")
    for mem in protected:
    	f.write("        "+mem+";\n")

    f.write("   private:\n")
    for mem in private:
    	f.write("        "+mem+";\n")
    
    f.write("};\n#endif")

    #closing header file
    f.close()
    
    #opening .cpp file
    f=open(DirSrc+'/'+name+'.cpp',"w+")

    #writing to .cpp file (#include and constructor/destructors)
    f.write("#include \""+name+".h\"\n")
    f.write(name+"::"+name+"()\n{\n\n}\n\n"+name+"::~"+name+"()\n{\n\n}")

    #closing .cpp file
    f.close

    mainM()
    
#new data member
def newDataMem():
    memb = input("Data Type and Name: ")
    
    encap=int(input("1. public\n2. private\n3. protected\n")) 

    if (encap==1):
        public.append(memb)
    elif (encap==2):
        private.append(memb)
    elif (encap==3):
        protected.append(memb)
    else:
        pass

#inheritance 
def relo():
    global parent

    parent=input("Parent Class Name:")
    inherType=int(input("1. public\n2. protected\n3. private\n"))

    if (inherType==1):
        parent = " : public "+parent
    elif (inherType==2):
        parent = " : protected "+parent
    elif (inherType==3):
        parent = " : private "+parent
    else:
        pass
    return

#setters and getters
def setget():
    #protected member setters
    for i in protected:
        splitter = i.split()
        dtype = splitter[0]
        dname = splitter[1]
        setrgetr.append("void set"+dname+"( "+dtype+" val ){ "+dname+"=val; }")
    
    #private member setters and getters
    for i in private:
        splitter = i.split()
        dtype = splitter[0]
        dname = splitter[1]
        setrgetr.append("void set"+dname+"( "+dtype+" val ){ "+dname+"=val; }")
        setrgetr.append( dtype+" get"+dname+"(){ return "+dname+"; }")
        
projectDir()

mainM()
