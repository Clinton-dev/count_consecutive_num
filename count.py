def solution(A):
    counter = 0
    B = [int(i)for i in A]
    print(B)
    y = []
    n = len(B)
    print(n)
    for x in range(n - 1):

        if (B[x] == B[x + 1]):
            y.append(B[x])
            counter += 1
        elif(B[x] != B[x + 1]) and (B[x] == B[x - 1]):
            y.append(B[x])

    return f'Occurs {y[0]} times {len(y)}'


print(solution('109999193'))
