def sum_func(n):
    s=0
    for x in range(1, n+1):
        s=s+x

    return s    # return을 for문 안으로 들여쓰기해서 하면 안된다.


print(sum_func(10))
print(sum_func(100))
