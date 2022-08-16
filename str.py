s = str(input())
s.upper()
#gua1 = 'g'
#cit1 = 'c'
if (gua1 == 'g') and (cit1 == 'c'):
    gua = s.count('g')
    cit = s.count('c')
    print(((gua+cit) / len(s)) * 100 )
elif (gua1 == 'G') and (cit1 == 'C'):
    gua = s.count('G')
    cit = s.count('C')
    print(((gua + cit) / len(s)) * 100)
elif (gua1 == 'G') and (cit1 == 'c'):
    gua = s.count('G')
    cit = s.count('c')
    print(((gua + cit) / len(s)) * 100)
elif (gua1 == 'g') and (cit1 == 'C'):
    gua = s.count('g')
    cit = s.count('C')
    print(((gua + cit) / len(s)) * 100)