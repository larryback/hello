import sys,os
print(sys.argv, len(sys.argv))

def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.platform]

sa = sys.argv
if len(sa) < 2 :
    sys.exit()

with open(sa[1], "r", encoding = "utf - 8") as file:
    for line in file:
        print(line)


def clear():


    if os.name == 'nt' :

        os.system('CLS')

    else:
    os.system('clear')    
