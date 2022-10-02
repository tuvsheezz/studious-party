def count_substring(a, b):
    n, m, j, c = len(a), len(b), 0, 0
    while(j < n):
        if(a[j] == b[0]):
            if(a[j:j + m] == b):
                c += 1
        j += 1

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
