a = input()
b = input()
print(a.find(b))
count = 0
while True:
    if b in a:
        count += 1
        a = a[a.find(b)+1:]
    else:
        break
print(count)