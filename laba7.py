def fur(s):
    return foor(s,0,0)
    
def foor(s,i,k):
    if i>=len(s):
        return k
    if s[i]=="а":
        k+=1
    return foor(s,i+1,k)
    
s=input()
print(fur(s))
