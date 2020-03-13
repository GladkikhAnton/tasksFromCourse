class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, obj):
        if obj>0 :
            super(PositiveList, self).append(obj)
        else:
            raise NonPositiveError