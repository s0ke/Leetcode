a=''
xx=str(x)
for i in range(len(xx)):
    a=xx[i]+a
if x>=0:
    if int(a)<=(2**31-1):
        return(int(a))
    else:
        return(0)
else:
    a='-'+a[:-1]
    if int(a)>=-2**31:
        return(int(a))
    else:
        return(0)
