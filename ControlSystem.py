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
        generateChildren(carState, root, 0)


    def generateChild(carState, layer, controls):
        #base case
        if(layer == self.numberOfIntervals):
            # this is the base case
            controls = getControls(oldCarState, carState)
            return Node(0, controls)
        obstacles = getObstaclesWithinDistance(carState)
        currentLane = carState.get_currentLane()
        # TODO: Does python pass by reference?
        # save the old car state to be used later
        oldCarState = copy.deepCopy(carState)
        if not obstacles:
            # create the next state, the 0 says just move forward as there are no obstacles around
            #create an empty control for this time
            #signifies that we aren't changing anything
            control = []
            # add the child to the tree
            # generate the state after the time interval passes
            carState = getNextState(carState, currentLane)
            controls.append(control)
            parent.addChild(generateChild(carState, layer + 1, controls))
            return parent
        # time to dodge these obstacles
        for lane in lanes:
            #TODO: if all possible lane changes result in a collision, slow down speed
            #generate the next state based on the lane change
            carState = getNextState(carState, lane)
            #generate the controls that would be needed to make the change happen
            control = getControls(oldCarState, carState)
            controls.append(control)
            parent.addChild(generateChild(carState, layer + 1, controls))
        return parent


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

    def scoreCurrentState(carState):
        if getObstaclesWithinDistance(carState, self.comfyDistanceToObstacle)


    #TODO: is calculating the euclidian distance only marginally slower?
    #This function finds all of the obstacles within a certain distance to the car
    def getObstaclesWithinDistance(carState, distance):
        obstaclesWithinDistance = []
        for obstacle in carState.objectLocations:
            # check if the object is within a euclidian distance to the object
            if(Math.sqrt(obstacle[0]^2 + obstacle[1]^2) > distance):
                obstaclesWithinDistance.append(obstacle)
        return obstaclesWithinDistance
