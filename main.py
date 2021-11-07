def fact(dic,n):
    if f'{n}' in dic:
        result = dic[f'{n}']
        return result
    if n < 2:
        result = n
        dic[f'{n}'] = result
    else:
        result =  fact(dic,n-1) + fact(dic,n-2)
        dic[f'{n}'] = result
    return result
print(fact({'0':0,'1':1},40))