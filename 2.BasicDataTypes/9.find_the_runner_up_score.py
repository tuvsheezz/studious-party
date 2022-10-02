if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    x = max(a)
    for i in range(0, n):
        if a[i] < x:
            print(a[i])
            break
