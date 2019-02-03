# try except 구문으로 예외를 처리합니다.
try:
    # 숫자로 변환합니다.
    number_input_a = int(input("정수 입력> "))
    # 출력합니다.
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
    print("예외가 발생하지 않았습니다.")
except:
    print("정수를 입력해달라고 했잖아요?!")
# 예외가 발생하든 발생하지 않든 실행됩니다.
print("일단 프로그램이 어떻게든 끝났습니다.")