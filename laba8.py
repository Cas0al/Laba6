def fur(s):
    return foor(s,0)
    
def foor(s,i):
    print(s,i,0)
    if i>=len(s):
        return s
    if s[i]=='z':
        s=s[:i]+"a"+s[i+1:]
    else:
        s=s[:i]+chr(ord(s[i])+1)+s[i+1:]
    print(s,i,1)
    return foor(s,i+1)
    
s=input()
print(fur(s))
