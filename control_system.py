from Node import Node
from State import State

# TODO: if it hits an object, stop going down that branch
# TODO: how do we handle turns when generating the next state?
# TODO: add delay hyper parameter
#hyperparamaters:
    #numberOfIntervals
    #timeInterval
    #comfyDistanceToObstacle

class ControlSystem(object):

    def __init__(self, timeInterval, numberOfIntervals, lanes, comfyDistanceToObstacle):
        """
        Initialize an instance of ControlSystem with specified parameters

        timeInterval:

        numberOfIntervals: This is the maximum number of time intervals allowed
        and can be thought of as the depth of the tree.

        lanes: this is the number of lanes within the track

        comfyDistanceToObstacle: This is the minimum distance we will allow the
        vehicles to be to an obstacle.

        collisionScore is the score applied when a vehicle comes within
        comfyDistanceToObstacle to an obstacle.

        distanceToWarrantTrim: This is a radius drawn around the car. We only
        care about obstacles within this radius, this reduces the number of
        possible calculations.

        """

        self.timeInterval = timeInterval
        self.numberOfIntervals = numberOfIntervals
        self.lanes = lanes
        self.comfyDistanceToObstacle = comfyDistanceToObstacle
        self.collisionScore = -1000

    def startTree(carState):
        """
        This function starts the creation of the tree of paths.

        carState: the initial state of the car before starting the search for
        an optimal path
        """
        root = Node(0, [])
        root.addChild(generateChildren(root, carState, 0, []))


    def generateChildren(parent, carState, layer, controls):
        """
        This is the base case for the recursion. We stop recursing and return
        a node with the controls to get there.
        """
        if(layer == self.numberOfIntervals):
            return Node(0, controls)

        """
        obtain an array of obstacles that exist within distanceToWarrantTrim of
        the vehicle.
        """
        obstacles = getObstaclesWithinDistance(carState, distanceToWarrantTrim)
        immediateObstacles = getObstaclesWithinDistance(carState, distanceToWarrantTrim/2)

        """
        retrieve the current lane of the vehicle
        """
        currentLane = carState.get_currentLane()

        """
        If there are no obstacles within the immediate vicinity, simply move forward
        """

        if not immediateObstacles:
            # generate the state after the time interval passes with no lane change
            futureCarState = getNextState(carState, currentLane)
            # get the controls to make the next state, this will return []
            control = getControls(carState, futureCarState)
            #append the controls to the controls array
            #This adds the controls for this time increment
            controls.append(control)
            # score the current state
            score = scoreState(carState, futureCarState)
            #this if statement should never be triggered
            #It is checking if we are colliding with an obstacle
            if score = self.collisionScore:
                continue
            #summate the score of the parent node and the child node
            score = score + parent.get_score()
            child = Node(score, controls)
            # add the reference to the new node
            # This recurses as well to create the children to be added
            child.addChildren(generateChild(child, futureCarState, layer + 1, controls))
            # return the child node to be added to its parent
            return [child]
        # create an empty list of children
        children = []
        """
        Iterate through all possible lane changes in order to create possible paths.
        """
        for lane in lanes:
            #generate the next state based on the lane change
            futureCarState = getNextState(carState, lane)
            #generate the controls that would be needed to make the change happen
            control = getControls(oldCarState, carState)
            controls.append(control)
            #score the current state
            score = scoreState(carState, futureCarState)

            #if this state is a collision, we want to terminate exploring this
            #branch
            if score = self.collisionScore:
                continue
            score = score + parent.get_score()
            #create the node for this state
            child = Node(score, controls)
            children.append(child)
            #append the children to the parent node
            parent.addChildren(generateChildren(carState, layer + 1, controls))
        #return the list of children
        return children


    # this is the dynamics function
    def getNextState(carState, lane):
        carState.set_currentLane(carState.get_currentLane + lane)
        #we don't need to change the position of the car itself as it is ego
        #centric
        #Calculate the translation and rotation to be applied to other obstacles
        translation = carState.getCurrentSpeed()*timeInterval
        if carState.isTurning():
            # a turning piece of track turns 45 degrees, so we take the
            # ratio of the distance traveled on the track and multiply it by 45
            turnInDegrees = translation/trackUnitLength * 45
            # create a rotation matrix based on the angle found in the previous line
            Rotation = [[cos(turnInDegrees), -sin(turnInDegrees)], [sin(turnInDegrees), cos(turnInDegrees)]]
        obstacles = []
        for obstacle in carState.get_objectLocations():
            # apply the transformation to the obstacles
            obstacle = Rotation*(obstacle - translation)
            obstacles.append(obstacle)
        carState.set_objectLocations(obstacles)
        return carState

    #generate the controls used to get from one state to another
    def getControls(carState, futureState):
        if futureState.get_currentLane = carState.get_currentLane:
            # if nothing changes, return an empty control vector
            return []
        else:
            return [futureState.get_currentLane]

    """
    This function returns the score of a given change in state.
    """
    def scoreState(previousState, carState, obstacles):
        score = 0
        #check to see if we are too close to any obstacles
        if getObstaclesWithinDistance(obstacles, self.comfyDistanceToObstacle):
            return self.collisionScore
        #if we change lanes, penalize for the largest lane changes
        if previousState.get_currentLane != carState.get_currentLane:
            #We use the squared difference between the current lane and the lane
            #we are changing too.
            score = ((previousState.get_currentLane)^2 - (carSTate.get_currentLane)^2)*-1

    #This function finds all of the obstacles within a certain distance to the car
    def getObstaclesWithinDistance(obstacles, distance):
        obstaclesWithinDistance = []
        for obstacle in obstacles:
            # check if the object is within a euclidian distance to the object
            if(Math.sqrt(obstacle[0]^2 + obstacle[1]^2) > distance):
                obstaclesWithinDistance.append(obstacle)
        return obstaclesWithinDistance

    """
    This function returns the node with the largest score.
    """
    def depthFirstSearch(node):
        temp = []
        # this is the base case for this recursive method
        if not node.get_children():
            return node
        for child in node.get_children():
             # recursive step
             temp.append(depthFirstSearch(child))
        largest = temp[0]
        # search through all of the children
        for item in temp:
            if largest.get_score < item.get_score():
                largest  = item
        return largest
