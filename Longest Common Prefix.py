prefix=""
if len(strs)==1:
    return(strs[0])
if strs[0]=='':
    return(prefix)
for i in range(len(strs[0])):
    prefix=prefix+strs[0][i]
    for j in strs:
        if len(j)>i:
            if j[i]!=strs[0][i]:
                prefix=prefix[:-1]
                return(prefix)
        else:
            prefix=prefix[:-1]
            return(prefix)
return(prefix)
