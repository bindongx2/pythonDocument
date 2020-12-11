import time         # 시간 관련된 기능

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()   # 현재 시간을 나타내는 함수

et = end - start
print("실제시간 : ", et , "초")
print("차이 : ", abs(et - 20) , "초")  # abs함수(절대값으로 값을 나타냄)
