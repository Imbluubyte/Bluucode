with open('script.txt', 'r') as f:
  code = f.readlines()

variables = {}
def printline(text):
  print(str(text))

def add(num1, num2):
  ans = int(num1) + int(num2)
  return int(ans)

def end():
  pass

def declare(variable, value):
  variables[variable] = value

def fetch(variable):
  return variables[variable]

def sub(num1, num2):
  ans = num1 - num2
  return ans 


syntax = {'printline': printline, 'add': add, 'declare': declare, 'sub': sub, 'fetch': fetch}

for line in code:
  args = []
  funcs = []
  components = line.split()
  for component in components:
    if component not in syntax:
      args.append(component)
    else:
      funcs.append(component)
  if len(funcs) != 0:
    if len(funcs) > 1:
      main_func = funcs[0]
      funcs.remove(main_func)
      secondary_funcs = {}
      for func in funcs:
        secondary_funcs[f'{func}'] = func
        for secondary_func in secondary_funcs:
          args.append(syntax[secondary_func](args[0], args[1]))
          args.remove(args[1])
          args.remove(args[0])
      syntax[main_func](args[0])
    else:
      func = funcs[0]
      syntax[func](args[0], args[1])






