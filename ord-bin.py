# 변수를 선언합니다.
input_a = list("Python")
print("기본 문자열:", input_a)

# 10진수를 출력합니다.
output_10 = []
for char in input_a:
    # ord(<문자>) => 10진수 값 출력
    output_10.append(ord(char))
print("10진수:", output_10)

# 2진수를 출력합니다.
output_2 = []
for char in input_a:
    output_2.append(bin(ord(char)))
print("2진수:", output_2)