class command():
    # def __init__(self,function,params, help,name,*args,**kwargs):

    #     self.function = function
    #     self.params = params
    #     self.help = help

    def evaluate(self, args):
        '''
        evaluate the command and check if it is goona be called
        '''
        if args[1] == self.function:
            self.function(**{self.args[2:]})
    def argsFormat(self, args):

        aux_args = args.copy()
        func_name = aux_args.pop()
        params = {}
        #get the keys
        for p in aux_args:
            if '-' in p:
                params[p] = None
        #get the values
        for i,p in enumerate(aux_args):
            if p in params:
                if i < len(aux_args):
                    if '-' not in args[i+1]:
                       params[p] = args[i+1]
        
        return {func_name:params}

obj = command()
print(obj.argsFormat(['app.py','test_function','-h','-name','genario','-last_name','nogueira']))






