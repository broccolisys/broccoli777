"""
 아이디어>
 정사각형 배열의 바깥쪽부터 안쪽으로 순차적으로 각 단계(q) 사각형 변 요소들의 값을 구합니다.
"""
def spiralarray(m,n):
    array,thick,length,q,level,value,x,y = [],m,m*n,0,0,0,0,0
    array = [[0 for h in range(n)] for i in range(m)]
    level = len(array)//2 + len(array)%2
    while q <= level:
        q += 1 # 사각형 단계 이동
# q단계 사각형 상단변 값 입력
        for a in range(y,n+y):
            if value == length:
                break
            array[x][a] = value
            value += 1
# q단계 사각형 우측변 값 입력
        for b in range(q,thick-q):
            if value == length:
                break
            array[b][thick-q] = value
            value += 1
# q단계 사각형 아랫변 값 입력
        for a in range(y,n+y):
            if value == length:
                break
            array[thick-q][-(a+1)] = value
            value += 1
# q단계 사각형 왼쪽변 값 입력
        for b in range(q+1,n+y):
            if value == length:
                break
            array[-b][y] = value
            value += 1
        x += 1
        y += 1
        n -= 2
    for sequence in array:
        new_sequence = ["%2s"%str(s) for s in sequence]
        print(' '.join(new_sequence),"\n")

if __name__ == "__main__":
    m = int(input("column = "))
    n = int(input("row = "))
    print("\n")
    spiralarray(m,n)