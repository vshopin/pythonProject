n = int(input())
if n >= 0:
    if n == 0:
        print(n, 'программистов')
    elif 10 <= n % 100 <= 20:
        print(n, 'программистов')
    elif n % 10 == 1:
        print(n, 'программист')
    elif 2 <= n % 10 <= 4:
        print(n, 'программиста')
    else:
        print(n, 'программистов')