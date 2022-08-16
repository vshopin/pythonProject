s = str(input())
if len(s) == 6:
    s1 = s[:1]
    s2 = s[1:2]
    s3 = s[2:3]
    s4 = s[3:4]
    s5 = s[4:5]
    s6 = s[5:6]
    sum1 = int(s1)+int(s2)+int(s3)
    sum2 = int(s4)+int(s5)+int(s6)
    if sum1 == sum2:
        print('Счастливый')
    else:
        print('Обычный')
