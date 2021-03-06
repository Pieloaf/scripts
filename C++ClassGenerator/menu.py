class Menu:

    def __init__(self,options,func):
        self.options = options
        self.func = func

    def __repr__(self):
        return ''.join(str(self.options.index(opt)+1) + '. ' + opt + '\n' for opt in self.options)
    
    def choice(self, chosen):
        self.func[(int(chosen)-1)]()