variables = {}

with open('script.txt', 'r') as f:
  code = f.readlines()
  
for line in code:
  components = line.split()
  if not components:
    continue
  if components[0] == 'print':
    text = ' '.join(components[1:])
    if text in variables:
      print(variables[text])
    else:
      print(text)
    
  elif components[0] == 'end':
    break
  elif components[0] == 'variable':
    variables[components[1]] = components[2]
  elif components[0] == 'add':
    if components[1] in variables and components[2] in variables:
      result = int(variables[components[1]]) + int(variables[components[2]])
    elif components[1] in variables:
      result = variables[components[1]] + components[2]
    elif components[2] in variables:
      result = components[1] + variables[components[2]]
    else:
      result = components[1] + components[2]
  else:
    print('Invalid Syntax')
