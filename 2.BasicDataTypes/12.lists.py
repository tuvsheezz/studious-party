if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        com, *a = input().split()
        com = com.lower()
        if com =='insert':
            l.insert(int(a[0]),int(a[1]))
        elif com =='print':
            print(l)
        elif com =='remove':
            l.remove(int(a[0]))
        elif com =='append':
            l.append(int(a[0]))
        elif com =='pop':
            l.pop()
        elif com =='sort':
            l.sort()
        elif com =='reverse':
            l.reverse()
