def complexNumberMultiply(a, b):
    a_comp=a.split('+')
    b_comp=b.split('+')
    a_comp[1]=a_comp[1][:len(a_comp[1])-1]
    b_comp[1]=b_comp[1][:len(b_comp[1])-1]
    ans=""
    ans=(str((int(a_comp[0])*int(b_comp[0]))-(int(a_comp[1])*int(b_comp[1]))))+"+"+(str((int(a_comp[0])*int(b_comp[1]))+(int(a_comp[1])*int(b_comp[0]))))+"i"
    return ans 

print(complexNumberMultiply("1+-1i", "1+-1i"))
