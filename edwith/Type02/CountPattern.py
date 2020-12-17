counts = dict() #딕셔너리 생성(배열)

file = open("CountPatternText.txt", encoding='UTF8')  # for문 돌려서 라인별로 가져와야함
han = file.read()    # 파일 전체 내용을 문자열로 가져옴
words = han.split()
print("words : " , words)
#for line in han:
#    line = line.strip()

for word in words:
    counts[word] = counts.get(word,0) + 1

print("Counts : ", counts)
