import run_system_functions
class file():
    def runfile(self,filepath:str):
        run_system_functions.run('JS', 1, False, True,filepath,'')
    def conv(self,code,mode,fscn):
        if mode == 'c':
            x = run_system_functions.run('JS', 1, False, True, '', code)
            print(x)
        if mode == 'cf':
            x = run_system_functions.run('JS', 1, False, True, '', code)
            w_fscn = open(fscn,'w')
            w_fscn.write(x)
        if mode == 'f':
            with open(fscn, 'r') as f:
                code = f.read()
            x = run_system_functions.run('JS', 1, False, True, '', code)
            print(x)
        if mode == 'ff':
            with open(fscn, 'r') as f:
                code = f.read()
            x = run_system_functions.run('JS', 1, False, True, '', code)
            w_fscn = open(fscn,'w')
            w_fscn.write(x)