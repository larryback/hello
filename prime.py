tot = 0
for num in range(101):
    if num == 2:  # 2는 소수이므로 바로 출력
        tot += num
    for x in range(2, num):  # 2부터 num-1까지 나누어 본다
            if num % x == 0:  # 나누어 떨어지면 소수가 아니므로 break
                break
            elif x == num - 1:  # num-1까지 나누어지지 않으면 소수
                tot += num
    print("Total sum of prime is {}".format(tot))