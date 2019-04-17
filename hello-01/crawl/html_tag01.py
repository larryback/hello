# p 태그로 감싸는 함수
def p(content):
    # 기존 코드 주석 처리
    # return "<p>{}</p>".format(content)
    # 2017.08.15 - 요청 반영
    return "<p class='content-line'>{}</p>".format(content)

# 출력합니다.
print(p("안녕하세요."))
print(p("간단한 HTML 태그를 만드는 예입니다."))