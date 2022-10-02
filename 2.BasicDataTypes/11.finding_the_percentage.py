if __name__ == '__main__':
    n = int(input())
    h = {}
    for _ in range(n):
        a, *line = input().split()
        s = sum(list(map(float, line))) / 3
        h[a] = s
    print("{:.2f}".format(h[input()]))
