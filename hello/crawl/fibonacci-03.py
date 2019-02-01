# 메모 변수를 만듭니다.
dictionary = {
    1: 1,
    2: 1
}

# 함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        # 메모 되어 있으면 메모 된 값 리턴
        return dictionary[n]
    else:
        # 메모 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
        # 흐름 중간에 return 키워드를 사용하는 것을 조기 return 이라고 부릅니다.