fh = open("mbox-short.txt")

for lx in fh:
    ly = lx.rstrip()  # 오른쪽 개행문자(\n 지우기)
    print(ly.upper())
