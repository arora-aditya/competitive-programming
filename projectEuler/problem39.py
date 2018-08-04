# https://projecteuler.net/problem=39

def integerRightTriangles():
    listing = [0]*1001
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = pow(i*i + j*j, 0.5)
            if i + j + k > 1000:
                continue
            if k - int(k) == 0:
                k = int(k)
                listing[i+j+k] += 1
    return max(listing), listing.index(max(listing))

print(integerRightTriangles())
