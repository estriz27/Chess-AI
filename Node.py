class Node(object):
    def __init__(self, data):
        self.data = data #
        self.children = [] #array of possible moves from that move
        self.leaf = True

    def add_child(self, obj):
        self.children.append(obj)

    def setIsLeaf(self):
        if len(self.children) > 0:
            self.leaf = False

    def getIsLeaf(self):
        return self.leaf




