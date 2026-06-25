import random
from pathlib import Path
import sys

def run_file(filename):
    global output_buffer

    output_buffer = []
    file = Path(filename)

    if not file.exists():
        raise Exception(f''' Could not find file: '{filename}' ''')

    if file.suffix != '.bluc':
        raise Exception('File format not supported. Use .bluc')

    with open(file, 'r') as f:
        script = f.readlines()
    
    for line in script:
        tokens = tokenize(line)
        if tokens:
            parse(tokens)
    return '\n'.join(output_buffer)

variables = {}
output_buffer = []

def printline(output):
    output_buffer.append(str(output))

def add(x, y):
    ans = int(x) + int(y)
    return ans

def sub(x, y):
    ans = int(x) - int(y)
    return ans

def declare(var, val):
    variables[var] = val

def rng(x, y):
    return random.randint(int(x), int(y))

def equal(x, y):
    return x == y




syntax = {
    'printline': printline,
    'add': add,
    'sub': sub,
    'declare': declare,
    'rng': rng,
    'equal': equal
}


def tokenize(line):
    tokens = []
    current = ''
    in_string = False
    for char in line:
        if char == '"':
            in_string = not in_string
            current += char
            continue
        
        if in_string:
            current += char
            continue



        if char in '(),':
            if current:
                tokens.append(current)
                current = ''
            
            if char != ' ':
                tokens.append(char)
        
        elif char == ' ':
            if current:
                tokens.append(current)
                current = ''
        
        else:
            current += char

    if current:
        tokens.append(current)
    
    return tokens
    


def parse(tokens):
    token = tokens.pop(0)

    if token in syntax:
        func = syntax[token]

        if tokens[0] != '(':
            raise Exception(f''' Expected '(' after {token}''')
        
        tokens.pop(0)

        args = []

        while tokens[0] != ')':
            if tokens[0] == ',':
                tokens.pop(0)
                continue

            args.append(parse(tokens))

        tokens.pop(0)

        return func(*args)
    
    if token in variables:
        return variables[token]
    
    try:
        return int(token)
    except ValueError:
        pass

    if token.startswith('"') and token.endswith('"'):
        return token[1: -1]
    

    return token


