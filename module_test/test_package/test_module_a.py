PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius


print("모듈파일입니다")
print(__name__)

# ./test_package/module_a.py의 내용
variable_a = "a 모듈의 변수"