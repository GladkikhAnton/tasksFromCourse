import json

temp = input()
tempdata = json.loads(temp)
data = {}
for i in range(len(tempdata)):
    child = tempdata[i]['name']
    for parent in tempdata[i]['parents']:
        if parent not in data:
            data[parent] = [child]
        else:
            data[parent].append(child)
    if child not in data.keys():
        data[child] = []
check = {}
nmb = {}
sort = []
for item in data.keys():
    check[item] = False
    sort.append(item)
sort.sort()
for nextItem in data.keys():
    stack = []
    stack.append(nextItem)
    weigth = 0
    while(len(stack)>0):
        length = len(stack)-1
        pop = stack.pop()
        if check[pop] == False:
            for i in data[pop]:
                if (i not in stack and check[i]==False):
                    stack.append(i)
                    weigth += 1
        check[pop] = True
    for i in check.keys():
        check[i] = False
    nmb[nextItem] = weigth+1
for item in sort:
    print(item, ':', nmb[item])





