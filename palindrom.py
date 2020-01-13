def palin(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palin(s, l+1, r-1)


print(palin("NitiN",0,len("NitiN")-1))
print(palin("Ashish",0,len("Ashish")-1))