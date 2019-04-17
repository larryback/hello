# 모듈을 읽어 들입니다.
import sys

# 명령 매개변수를 출력합니다.
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

import sys

print("argv size :", len(sys.argv))

for i, arg in enumerate(sys.argv):

        print(i, arg)



# 프로그램을 강제로 종료합니다.
sys.exit()