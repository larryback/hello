with open("test.txt", "w") as file:
    # writeline() 기본 사용
    file.writelines(["안녕하세요.",\
        "줄바꿈이 될까요",\
        "안될까요?",\
        "띄어쓰기라도 들어가주지 않을까요?"])

    # writeline() 매개변수의 리스트는 여러 자료형을 가질 수 있을까?
    file.writelines([True, 273, "문자열"])