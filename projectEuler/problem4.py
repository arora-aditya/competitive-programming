max_pal = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        ij = i*j
        if str(ij) == str(ij)[::-1]:
            if ij > max_pal:
                max_pal = ij
print(max_pal)
