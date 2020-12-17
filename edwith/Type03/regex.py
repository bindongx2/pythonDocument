import re

hand  = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    # 정규식
    #  ^ : 줄의 시작을 의미
    #  . : 임의의 아무 문자와도 매칭되는 와일드 카드
    # \S : 공백이 아닌 문자
    #  + : 한번 이상 나온다는 뜻
    if re.search('^From:', line):
    # if line.startswith("From:") 같은의미
        print(line)
