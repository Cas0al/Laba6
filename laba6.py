def f6(s):
    s=s.capitalize()
    k=s.index(" ")
    s0=s[:k]+" "
    s=s[k+1:]
    k=s.index(" ")
    s0+=s[0].capitalize()+"."+s[k+1].capitalize()+"."
    return s0
    

s=input()
print(f6(s))
