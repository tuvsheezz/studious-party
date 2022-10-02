def swap_case(s):
    r = ""
    for c in s:
        if c.islower():
           r += c.upper()
        elif c.isupper():
           r += c.lower()
        else:
            r += c
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
