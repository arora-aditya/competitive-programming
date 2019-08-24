def triangle(x):
    return (x * (x+1))//2

def pentagonal(x):
    return (x * (3*x - 1))//2

def hexagonal(x):
    return x * (2*x - 1)
    
triangles = set([triangle(x) for x in range(285 + 1000000)])
pentagonals = set([pentagonal(x) for x in range(165 + 100000)])
hexagonals = set([hexagonal(x) for x in range(143 + 100000)])

print(list(triangles & pentagonals & hexagonals)[3])