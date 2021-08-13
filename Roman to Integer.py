a=0
for i in range(len(s)):
    if s[i]=='I':
        a=a+1
    if i<(len(s)-1):
        if s[i]=='I':
            if s[i+1]=='V' or s[i+1]=='X':
                a=a-2
        if s[i]=='X':
            if s[i+1]=='C' or s[i+1]=='L':
                a=a-20
        if s[i]=='C':
            if s[i+1]=='M' or s[i+1]=='D':
                a=a-200
    if s[i]=='V':
        a=a+5
    if s[i]=='X':
        a=a+10
    if s[i]=='L':
        a=a+50
    if s[i]=='C':
        a=a+100
    if s[i]=='D':
        a=a+500
    if s[i]=='M':
        a=a+1000
return(a)
