def BubbleSort_short(L:list):
    n = len(L)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    print(L)

def BubbleSort_long(L:list):
    n = len(L)
    exchange = True
    while exchange:
        exchange = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                exchange = True
    print(L)