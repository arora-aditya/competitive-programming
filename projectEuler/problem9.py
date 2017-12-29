for i in range(1,1000):
    for j in range(1,1000-i):
        if pow(i,2) + pow(j,2) == pow(1000-i-j,2):
            print(i,j,1000-i-j)
