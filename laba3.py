def fr3(s):
    s=s.replace(" ","")
    s=s.lower()
    if s==s[::-1]:
        return "Да"
    return "Нет"
s=input()
print(fr3(s))
