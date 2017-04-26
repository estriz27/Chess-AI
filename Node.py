class Node(object):
    def __init__(self, data):
        self.data = data #
        self.children = [] #array of possible moves from that move

    def add_child(self, obj):
        self.children.append(obj)
