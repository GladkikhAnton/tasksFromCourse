import itertools

def primes():
    x = []
    simpleNum = 1
    while True:
        simpleNum += 1
        for num in x:
            if simpleNum % num == 0:
                break
        else:
            x.append(simpleNum)
            yield simpleNum
print(list(itertools.takewhile(lambda x : x <= 31, primes())))