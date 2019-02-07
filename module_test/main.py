# import test_package.test_module_a as a
# import test_package.test_module_c as c

# # 모듈 내부의 변수를 출력합니다.
# print(a.variable_a)
# print(c.variable_c)

#################################################

# "from test_package import *"로
# 모듈을 읽어 들일 때 가져올 모듈
__all__ = ["test_module_a", "test_module_c"]

# 패키지를 읽어 들일 때 처리를 작성할수도 있습니다.
print("test_package를 읽어 들였습니다.")