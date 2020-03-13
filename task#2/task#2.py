class Buffer:
    def __init__(self):
        self.list = []

    def add(self, *a):
        sum = 0
        for item in a:
            self.list.append(item)
            while len(self.list) >= 5:
                # print('while')
                for s in range(0,5):
                    sum += self.list[s]
                print(sum, end=" ")
                sum = 0
                for s in range(0,5):
                    del self.list[0]
        print()

    def get_current_part(self):
        return self.list
