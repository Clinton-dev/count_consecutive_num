# ! python 3.9.13
def solution(A):
    """
    A function that takes in a string of numbers and returns the larges number
    that occurs consecutively in a string
    """
    B = [int(i)for i in A]
    print(B)
    y = []
    count = dict()
    n = len(B)
    print(n)
    for x in range(n-1):

        if (B[x] == B[x + 1]):
            y.append(B[x])
        elif(B[x] != B[x + 1]) and (B[x] == B[x - 1]):
            y.append(B[x])
    print(y)
    k = len(y)
    for i in range(k):
        if y[i] in count.keys():
            count[y[i]] += 1
        else:
            count[y[i]] = 1

    max_key = max(count, key=count.get)

    value = count.get(max_key)

    return f'{max_key}.Occurs {value}times'


print(solution('10121116'))
print(solution('109999193'))
