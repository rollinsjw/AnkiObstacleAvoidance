class Node(object):

    # initiates a node
    def __init__(self, score, controls):
        """
        controls: [c1, c2, c3, c4], in order to get from the state at time 0, to
        the state at time 4, we execute c1 at time 0, c2 at time 1, c3 at time 2
        and c4 at time 3. The index at which a control sits in the array corresponds
        to the time interval at which it should be executed

        score: The score of a node is the cumulative score of the path to get to
        that node.

        children: the children
        """
        self.score = score
        self.children = []
        self.controls = controls

    # adds a child to the node
    def addChild(self, child):
        self.children.append(child)

    # add multiple children to the same child
    def addChildren(self, children):
        for child in children:
            self.children.append(child)


    # getters 
    def get_score(self):
        return self.score

    def get_controls(self):
        return self.controls

    def get_children(self):
        return self.children
