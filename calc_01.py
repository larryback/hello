def add():
    num = int(input("num1:"))
    num2 = int(input("num2:"))
    result = num + num2
    print(result)

def sub():
    num = int(input("num1:"))
    num2 = int(input("num2:"))
    result = num - num2
    print(result)

def multiply():
    num = int(input("num1:"))
    num2 = int(input("num2:"))
    result = num * num2
    print(result)

def divide():
    num = int(input("num1:"))
    num2 = int(input("num2:"))
    if num ==0 or num2 == 0:
        print("Error")
        return
    result = num / num2
    print(result)

while True:
    print("  Menu  ")
    print("--------")
    print(" 1: add ")
    print(" 2: sub ")
    print(" 3: multiply")
    print(" 4: divide")
    print(" 5: stop")
    sel = int(input(":"))

    if(sel == 1):
        add()
    elif(sel == 2):
        sub()
    elif(sel == 3):
        multiply()
    elif(sel == 4):
        divide()        
    elif(sel ==5):
        break
    else:
        print("Wrong input, please input again")