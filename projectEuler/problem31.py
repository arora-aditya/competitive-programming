# https://projecteuler.net/problem=31

# BruteForce solution
def dfs(sum, path, paths):
    if sum < 0:
        pass
    elif sum == 0:
        paths.append(path)
    else:
        paths = dfs(sum-1,path+[1], paths)
        paths = dfs(sum-2,path+[2], paths)
        paths = dfs(sum-5,path+[5], paths)
        paths = dfs(sum-10,path+[10], paths)
        paths = dfs(sum-20,path+[20], paths)
        paths = dfs(sum-50,path+[50], paths)
        paths = dfs(sum-100,path+[100], paths)
        paths = dfs(sum-200,path+[200], paths)
    return paths

# optimised pro solution
coins = [1,2,5,10,20,50,100,200]
li = [0]*201
li[0] = 1
for i in coins:
    for j in range(i,201):
        li[j] += li[j - i];
print(li[200])
