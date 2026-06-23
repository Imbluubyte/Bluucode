with open('script.txt', 'r') as f:
    script = f.readlines()

variables = {}

def printline(output):
    print(output)

def add(num1, num2):
    ans = int(num1) + int(num2)
    return ans

def sub(num1, num2):
    ans = int(num1) - int(num2)
    return ans

def dec(var, val):
    variables[var] = val


_printline = {'args': 1, 'func': printline}
_add = {'args': 2, 'func': add}
_sub = {'args': 2, 'func': sub}
_dec = {'args': 2, 'func': dec}

syntax = {
    'printline': _printline,
          'add': _add,
          'sub': _sub,
          'dec': _dec,
    }

for line in script:
    args = []
    funcs = []
    func_args = []
    components = line.split()
    if not components:
        continue
    for component in components:
        if component not in syntax:
            if component in variables:
                args.append(variables[component])
            else:
                args.append(component)
        else:
            funcs.append(component)
    
    if len(funcs) > 1:
        main_func = funcs[0]
        funcs.remove(main_func)
        for func in funcs:
            if len(args) != syntax[func]['args']:
                print(f'''Error: function '{func}' expected {syntax[func]['args']} arguments. Recieved {len(args)}''')
            
            else:
                func_args.append(syntax[func]['func'](*args))
        syntax[f'{main_func}']['func'](*func_args)
    else:
        syntax[funcs[0]]['func'](*args)

    
         

        



                
