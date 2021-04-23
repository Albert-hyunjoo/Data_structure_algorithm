class SimpleTree(object):
    def __init__(self, value = None, children = None):
        self.value = value
        self.children = children
        if self.children is None:
            self.children = []
    def __repr__(self, level = 0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

st = SimpleTree("a", [SimpleTree("b", [SimpleTree("d"), SimpleTree("f")]), SimpleTree("c")])
print(st)