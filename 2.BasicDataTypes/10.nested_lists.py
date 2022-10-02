if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        a.append([input(), float(input())])
    
    ss = sorted(set([y for x, y in a]))[1]
    print('\n'.join(sorted([x for x, y in a if y == ss])))
