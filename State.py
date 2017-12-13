class State:
    # this class is the state class, it is egocentric so it will be instantiated
    # for each item on the track
    def __init__(self, data):
            self.uid = data["carUID"]
            self.currentLane = data["currentLane"]
            self.currentSpeed = data["currentSpeed"]
            self.currentAcceleration = data["currentAcceleration"]
            self.isTurning = data["isTurning"]
            self.carImFollowing = data["carImFollowing"]
            self.objectLocations = data["objectLocations"]
            self.isCar = data["isCar"]
            self.currentPosition = data["currentPosition"]
            self.directionVector = data["directionVector"]

    #TODO: function to get location of other objects relative to this object


#    setters and getters
    def get_uid(self):
        return self.uid
    def set_uid(self, uid):
        self.uid = uid

    def get_currentLane(self):
        return self.currentLane
    def set_currentLane(self, lane):
        self.currentLane = lane

    def get_currentSpeed(self):
        return self.currentSpeed
    def set_currentSpeed(self, speed):
        self.currentSpeed = speed

    def get_currentAcceleration(self):
        return self.currentAcceleration
    def set_currentAcceleration(self, acceleration):
        self.currentAcceleration = acceleration

    def get_isTurning(self):
        return self.isTurning
    def set_isTurning(self):
        if self.isTurning = True:
            self.isTurning = False
        else:
            self.isTurning = True

    def get_carImFollowing(self):
        return self.carImFollowing
    def set_carImFollowing(self, car):
        self.carImFollowing = car

    def get_objectLocations(self):
        return self.objectLocations
    def set_objectLocations(self, objects):
        self.objectLocations = objects

    def get_isCar(self):
        return self.isCar
    def set_isCar(self, isCar):
        self.isCAr = isCar

    def get_currentPosition(self):
        return self.currentPosition
    def set_currentPosition(self, position):
        self.currentPosition = position

    def get_directionVector(self):
        return self.directionVector
    def set_directionVector(self, vector):
        self.directionVector = vector
