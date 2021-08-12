xx=str(x)
flag=1
for i in range(len(xx)):
    if xx[i]!=xx[-i-1]:
        flag=-1*flag
        break
if flag>0: 
    return True
else:
    return False
