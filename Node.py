class Node(object):

    # initiates a node
    def __init__(self, score, controls):
        self.score = score
        self.children = []
        self.controls = controls

    # adds a child to the node
    def addChild(self, child):
        self.children.append(child)

    def addChildren(self, children):
        for child in children:
            self.children.append(child)

    def get_score(self):
        return self.score

    def get_controls(self):
        return self.controls

    def get_children(self):
        return self.children
