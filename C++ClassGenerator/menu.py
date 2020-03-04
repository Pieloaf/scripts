class Menu:

    def __init__(self,options,func):
        self.options = options
        self.func = func

    def __repr__(self):
        options_list = '\n'.join(str(self.options.index(option)+1) + '. ' + option for option in self.options)
        return options_list
    
    def choice(self, chosen):
        x = int(chosen)
        why = self.func[(x-1)]
        why()
