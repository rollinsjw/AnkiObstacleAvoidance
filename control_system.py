from Node import Node
from State import State

# TODO: how do we handle turns when generating the next state?
#hyperparamaters:
    #manhattanDistanceToObstacles
    #numberOfIntervals
    #timeInterval
    #comfyDistanceToObstacle

class ControlSystem(object):

    #initialization function that doens't really do anything
    def __init__(self, timeInterval, numberOfIntervals, manhattanDistanceToObstacle, lanes, comfyDistanceToObstacle):
        self.timeInterval = timeInterval
        self.numberOfIntervals = numberOfIntervals
        self.manhattanDistanceToObstacle = manhattanDistanceToObstacle
        self.lanes = lanes
        self.comfyDistanceToObstacle = comfyDistanceToObstacle

    # initialize the tree
    def startTree(carState):
        root = Node(0, [])
        root.addChild(generateChildren(root, carState, 0, []))


    def generateChildren(parent, carState, layer, controls):
        #base case
        if(layer == self.numberOfIntervals):
            # this is the base case
            return Node(0, controls)
        obstacles = getObstaclesWithinDistance(carState, distanceToWarrantTrim)
        currentLane = carState.get_currentLane()
        if not obstacles:
            # generate the state after the time interval passes with no lane change
            futureCarState = getNextState(carState, currentLane)
            # get the controls to make the next state, will return []
            control = getControls(carState, futureCarState)
            controls.append(control)
            # score the current state
            score = scoreCurrentState(carState, futureCarState)
            child = Node(score, controls)
            # add the reference to the new node
            child.addChildren(generateChild(child, futureCarState, layer + 1, controls))
            # return the child node to be added to its parent
            return [child]
        # time to dodge these obstacles
        # create a list of children
        children = []
        for lane in lanes:
            #TODO: if all possible lane changes result in a collision, slow down speed
            #generate the next state based on the lane change
            futureCarState = getNextState(carState, lane)
            #generate the controls that would be needed to make the change happen
            control = getControls(oldCarState, carState)
            controls.append(control)
            score = scoreCurrentState(carState, futureCarState)
            child = Node(score, controls)
            children.append(child)
            parent.addChildren(generateChildren(carState, layer + 1, controls))
        return children


    # this is the dynamics
    # TODO: finish the dynamics
    def getNextState(carState, lane):
        carState.set_currentLane(lane)
        # TODO: use directionVector to calculate an estimate of where the car will be
        position =
        carState.set_currentPosition()

    #generate the controls used to get from one state to another
    def getControls(carState, futureState):
        if futureState.get_currentLane = carState.get_currentLane:
            return []
        else:
            return [futureState.get_currentLane]

    def scoreCurrentState(previousState, carState, obstacles):
        #check to see if we are too close to any obstacles
        score = 0
        if getObstaclesWithinDistance(obstacles, self.comfyDistanceToObstacle):
            return -10000
        #if we change lanes, penalize for the largest lane changes
        if previousState.get_currentLane != carState.get_currentLane:
            score = ((previousState.get_currentLane)^2 - (carSTate.get_currentLane)^2)*-1




    #TODO: is calculating the euclidian distance only marginally slower?
    #TODO: calculate the distance from box
    #This function finds all of the obstacles within a certain distance to the car
    def getObstaclesWithinDistance(obstacles, distance):
        obstaclesWithinDistance = []
        for obstacle in obstacles:
            # check if the object is within a euclidian distance to the object
            if(Math.sqrt(obstacle[0]^2 + obstacle[1]^2) > distance):
                obstaclesWithinDistance.append(obstacle)
        return obstaclesWithinDistance
