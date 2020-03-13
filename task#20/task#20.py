import csv
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    check = {}
    for item in reader:
        if item[5] not in check.keys():
            check[item[5]] = 0
        else:
            check[item[5]] += 1
    max = 0
    answer = ''
    for item in check.keys():
        if max < check[item]:
            max = check[item]
            answer = item
    print(answer)