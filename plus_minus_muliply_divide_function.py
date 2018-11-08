def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return a

    return a / b 

cmd = input("Input(usage: a + b)>>")

cmds = cmd.split(" ")

#a = int(cmds[0])
#b = int(cmd[2])
#op = cmds[1]

a, op, b =cmds

a, b = int(a), int(b)

r = 0
if op == '+':
    r = plus(a, b)

elif op == '-':
    r = minus(a, b)

elif op == '-':
    r = multiply(a, b)

else:
    r = divide(a, b)

if op == '/':
     print("Answer is {:.2f}".format(r))

else:
     print("Answer is {:d}".format(r))
 

