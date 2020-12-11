str = 'X-DSPAM-confidence: 0.8475  '
print(str)

str1 = str.find(":")  # str 문자열에서 : 위치 찾기
print(str1)

str2 = str[str1+1:]   # :위치부터 맨 끝까지 문자열 출력
print(str2)

str3 = str2.strip()   # 처음 문자열과 마지막 문자열에 공백 제거
print(str3)
