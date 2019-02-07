# 패키지 내부의 모듈을 읽어 들입니다.
import test_package.test_module_a as a
import test_package.test_module_c as c

# 모듈 내부의 변수를 출력합니다.
print(a.variable_a)
print(c.variable_c)