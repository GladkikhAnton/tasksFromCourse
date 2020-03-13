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
q = int(input())
for i in range(q):
    stack = []
    stop = True
    parent, children = input().split()
    stack.append(children)
    while(len(stack)>0 and stop):
        if children==parent:
            stop = False
            print('Yes')
            break
        if len(abj[children])==0:
            check[children]=True
            stack.pop()
        elif check[children]==False:
            for item in abj[children]:
                if item == parent:
                    stop = False
                    print('Yes')
                    break
                if check[item] == False:
                    stack.append(item)
            check[children]=True
        else:
            stack.pop()
        line = len(stack)
        if(len(stack)>=1):
            children=stack[line-1]
    if stop:
        print('No')
    for key in check.keys():
        check[key] = False