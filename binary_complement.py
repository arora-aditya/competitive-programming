def binary_complement(x):
    x_bin="{0:b}".format(x)
    y_bin=""
    for i in x_bin:
        if i=='0':
            y_bin += '1'
        else:
            y_bin += '0'
    return int(y_bin,2)

x=input("Enter a number:")
print(binary_complement(int(x)))
