cmd = input("Input(usage: 이름, 나이, 성별)>> ")
print(cmd)
cmds = cmd.split(",")


cmd = 0

# 1. 값이 존재하는 여부 체크 
if cmd == "":
    print("정확히 입력해 주세요")
    exit()

# 2. , 가 있는지 여부 체크 
if  "," not in cmd:
    print("컴마로 구분해서 써주세요")
    exit()

# 3. 3개의 값이 있는지 여부 if cmd.find(",") == -1
if  len(cmds) != 3:
    print("3개의 값을 넣어주세요")
    exit()

outmsg = "당신의 이름 {}, 나이는 {}, 성별은 {} 입니다"

print(outmsg.format(cmds[0], cmds[1], cmds[2]))    

