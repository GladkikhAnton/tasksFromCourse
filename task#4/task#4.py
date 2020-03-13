import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(list, Loggable):
    def append(self, obj):
        super(LoggableList, self).append(obj)
        self.log(obj)
x = LoggableList([1,2,3])
print(x)
x.append(2)
print(x)
print(type(LoggableList.mro()))