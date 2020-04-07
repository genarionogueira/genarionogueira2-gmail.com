class command():
    def __init__(self,function,name,params,*args,**kwargs):

        self.function = function
        self.name = name
        self.params = params        

    def evaluate(self, args):
        '''
        evaluate the command and check if it is goona be called
        '''
        if args[1] == self.function:
            self.function()

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

def hello_world(name):
    print('Hello World {name}'.format(name))

import sys
if __name__=="__main__":
    cmdHelloWorld = command(hello_world,'mycmdhelloworld',{'name':' Name that is going to be printed '})
    cmdHelloWorld.evaluate(sys)




