def leng(s):
    if len(s)<5:
        return "Короткая"
    elif 5<=len(s)<=10:
        return "Средняя"
    else:
        return "Длинная"

s=input()
print(leng(s))
