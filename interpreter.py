import inspect
import random

with open('script.txt', 'r') as f:
    script = f.readlines()

variables = {}

def printline(output):
    print(output)

def add(x, y):
    ans = int(x) + int(y)
    return ans

def sub(x, y):
    ans = int(x) - int(y)
    return ans

def declare(var, val):
    variables[var] = val

def rng(num1, num2):
    return random.randint(num1, num2)

syntax = {
    'printline': printline,
    'add': add,
    'sub': sub,
    'declare': declare,
    'rng': rng
}

def parse(tokens):
    token = tokens.pop(0)
    

    if token in syntax:
        func = syntax[token]

        arg_count = len(inspect.signature(func).parameters)
        args = []

        for _ in range(arg_count):
            args.append(parse(tokens))
        
        return func(*args)
    
    if token in variables:
        return variables[token]
    
    return token

for line in script:
    tokens = line.split()

    if not tokens:
        continue

    parse(tokens)