import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()

for line in fhand:
    print("line : ", line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print("counts : ", counts)


fhand2 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line2 in fhand2:
    print(line2.decode().strip())

#크롤러는 웹페이지를 읽어와 웹크롤러 데이터베이스에 저장합니다.
