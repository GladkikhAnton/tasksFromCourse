import datetime
year, month, day = map(int, input().split())
x = datetime.datetime(year, month, day)
dayPlus = int(input())
y = datetime.timedelta(dayPlus)
answer = x + y
print(answer.year, answer.month, answer.day)