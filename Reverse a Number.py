n = int(input())

while(n > 0):
    a = n % 10
    print(a)
    n = int(n / 10)    # int is used because n value should only be integer not float