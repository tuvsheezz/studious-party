def print_formatted(q):
    x = len("{0:b}".format(q))
    for i in range(1, q+1):
        bi = "{0:b}".format(i)
        oc = "{:o}".format(i)
        he = "{:x}".format(i)
        print(f"{str(i).rjust(x)} {str(oc).rjust(x)} {str(he).upper().rjust(x)} {bi.rjust(x)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
