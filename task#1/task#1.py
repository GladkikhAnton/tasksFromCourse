n = int(input())

parents = {'global':[None]}
values = {}
def create(namespace, parent):
    if namespace in parents.keys():
        parents[namespace].append(parent)
    else:
        parents[namespace] = [parent]
def add(namespace, var):
    if namespace in values.keys():
        values[namespace].append(var)
    else:
        values[namespace] = [var]
def get(namespace,var):
    if namespace==None:
        print('None')
        return 'None'
    if namespace in values.keys():
        if var in values[namespace]:
            print(namespace)
            return 'stop'
    return get(parents[namespace][0], var)
for i in range(n):
    action, namespace, value = input().split()
    if action == 'add':
        add(namespace, value)
    if action == 'create':
        create(namespace, value)
    if action == 'get':
        get(namespace, value)