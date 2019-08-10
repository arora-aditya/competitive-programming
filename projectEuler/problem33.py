from fractions import Fraction
ans = [1,1]

for i in range(10, 99):
    for j in range(i+1, 99):
        numerator = set(str(i))
        denominator = set(str(j))
        if numerator & denominator and numerator & denominator != {'0'}:
            f = Fraction(i, j)
            simplified_numerator = f.numerator
            simplified_denominator = f.denominator
            
            common = numerator & denominator
            new_numerator = list(numerator - common)
            new_denominator = list(denominator - common)
            if len(new_numerator) == 1 and len(new_denominator) == 1:
                try:
                    f_new = Fraction(int(new_numerator[0]), int(new_denominator[0]))
                    if f == f_new:
                        # print(i,j,f)
                        # print(i,j,ans)
                        ans = [ans[0]*i, ans[1]*j]
                except:
                    pass
                    # print('-'*50+'>',i, j)
print(Fraction(ans[0], ans[1]).denominator)