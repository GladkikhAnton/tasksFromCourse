s = input()
a = input()
b = input()
count = 0
while True:

    if count > 1000:
        print("Impossible")
        break
    if a in s:
        s = s.replace(a, b)
        count += 1
    else:
        break
if count <= 1000:
    print(count)