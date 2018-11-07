def plus(a,b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b 

cmd = input("Input(usage: a, b)>>")
print(cmd)
cmds = and.split(",")
a = int(cmds[0])
b = int(cmd[2])
op = cmds[1]

if op == '+':
    r = plus(a, b)
elif op == '-'
print("Answer is ", r)

print(format(cmds[0], cmds[1]))    

