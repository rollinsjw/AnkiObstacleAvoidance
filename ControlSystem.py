from Node import Node
from State import State

# TODO: how do we handle turns when generating the next state?
#hyperparamaters:
    #manhattanDistanceToObstacles
    #numberOfIntervals
    #timeInterval

class ControlSystem(object):

    #initialization function that doens't really do anything
    def __init__(self, timeInterval, numberOfIntervals, manhattanDistanceToObstacle, lanes):
        self.timeInterval = timeInterval
        self.numberOfIntervals = numberOfIntervals
        self.manhattanDistanceToObstacle = manhattanDistanceToObstacle
        self.lanes = lanes

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
        carState.set_

    #generate the controls used to get from one state to another
    def getControls(carState, futureState):

    def scoreCurrentState(carState):

    #this is done with manhattan distance in order to minimize computational effort
    #TODO: is calculating the euclidian distance only marginally slower?
    #This function finds all of the obstacles within a certain distance to the car
    def getObstaclesWithinDistance(carState):
        obstaclesWithinDistance = []
        for obstacle in carState.objectLocations:
            if(obstacle[0] + obstacle[1] > self.manhattanDistanceToObstacle):
                obstaclesWithinDistance.append(obstacle)
        return obstaclesWithinDistance

    def calculateEuclidianDistance(obstacleCoords):
        #TODO: find the syntax for this
        return Math.sqrt(obstacleCoords[0]**2 + obstacleCoords[1]**2)
