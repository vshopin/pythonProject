s = str(input())
gua = s.upper().count('G')
cit = s.upper().count('C')
print(((gua+cit) / len(s)) * 100 )
