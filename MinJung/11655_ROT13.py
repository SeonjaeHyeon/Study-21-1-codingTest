str= input()
new = []
for i in list(str):
    if i in "0123456789 ":
        new.append(i)
    else:
        asc = ord(i)
        if asc>=65 and asc<=90:
            asc+=13
            if asc>90:
                asc-=26
            new.append(chr(asc))
        else:
            asc+=13
            if asc>122:
                asc-=26
            new.append(chr(asc))
for i in new:
    print(i, end = '')