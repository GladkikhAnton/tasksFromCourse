class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.lst = iterable
        self.check = []
        for item in funcs:
            self.check.append(item)
        self.ju = judge

    def __iter__(self):
        for item in self.lst:
            pos = 0
            neg = 0
            for func in self.check:
                if func(item):
                    pos += 1
                else:
                    neg += 1
            if self.ju(pos, neg):
                yield item
