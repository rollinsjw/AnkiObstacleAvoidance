class Node(object):

    # initiates a node
    def __init__(self, rating, controls):
        self.rating = data["rating"]
        self.children = []
        self.controls = data["controls"]

    # adds a child to the node
    def addChild(self, child):
        self.children.append(child)

    def addChildren(self, children):
        for child in children:
            self.children.append(child)
