# https://projecteuler.net/problem=40

def champernowne():
    st = "0"
    for i in range(1,1000000):
        st += str(i)
    print()
    print(st[1], st[10], st[100], st[1000], st[10000], st[100000], st[1000000])
    return int(st[1]) * int(st[10]) * int(st[100]) * int(st[1000]) * int(st[10000]) * int(st[100000]) * int(st[1000000])

print(champernowne())
