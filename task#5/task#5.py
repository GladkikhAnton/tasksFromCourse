n = int(input())
abj = {}
check = {}
for i in range(n):
    a, *b = input().split(" ")
    if a not in abj.keys():
        abj[a]=[]
        check[a] = False
    for item in b:
        if item == ':':
            continue
        abj[a].append(item)
        if item not in abj.keys():
            abj[item] = []
            check[item] = False
q = int(input())
dictForExc = []
for i in range(q):
    stack = []
    update = True
    exception = input()
    stack.append(exception)
    stop = True
    while (len(stack) > 0 and stop):
        lastItem = stack[len(stack)-1]
        if lastItem in dictForExc:
            update = False
            stop = False
            break
        if len(abj[lastItem]) == 0:

            check[lastItem] = True
            stack.pop()
        elif check[lastItem] ==  False:
            for item in abj[lastItem]:
                if len(abj[item]) == 0:
                    check[item]=True
                if check[item] == False:
                    stack.append(item)
                if item in dictForExc:
                    print(exception)
                    update = False
                    stop = False
                    break
            check[lastItem] = True
        else:
            stack.pop()
    if update:
        dictForExc.append(exception)
    for key in check.keys():
        check[key] = False