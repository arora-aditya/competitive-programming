save = {}
def eval(i, save):
    sa = i
    le = 1
    while i != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = (3 * i) + 1
        if i in save:
            le += save[i]
            break;
        else:
            le+=1
    save[sa] = le
    return le
ma = 0
for i in range(1,1000000):
    lei = eval(i,save)
    if ma < lei:
        ma = lei
        sa = i
    # if i%10000 == 0:
    #     print(save, lei)
print(ma, sa)
