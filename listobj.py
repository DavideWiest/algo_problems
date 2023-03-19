import functools

class ListObj():
    def __init__(self, l):
        self.l = l

    def map(self, fn):
        return ListObj(map(fn, self.l))
    
    def filter(self, fn):
        return ListObj(filter(fn, self.l))
    
    def reduce(self, fn):
        return functools.reduce(fn, self.l)
    
    def withItem(self, item):
        return ListObj(self.l + [item])
    
    def cloneWithVariations(self, variableItemsToAppend):
        return [
            self.withItem(item) for item in variableItemsToAppend
        ]
    
    def __contains__(self, item):
        return item in self.l