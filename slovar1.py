d = {}
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value) # добавит значение в список по ключу
    else:
        if key * 2 in d:
            d[key * 2].append(value) # добавит значение в список по ключу
        else:
            d[key * 2] = [value] # давбавит ключ в словарь и сопоставит ему значение  которое передается в словаре
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}