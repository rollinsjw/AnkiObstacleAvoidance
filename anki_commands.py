import subprocess
import shlex
# TODO: make this more extensible, so n cars could be used
class Anki:

    #instantiates the c programs the communicate with the cars
    def __init__(carsMacs, mac1, mac2, laneChangeSpeed, laneChangeAcceleration):
        # TODO: change the permissions of the file to avoid having to sudo?
        # PaperNote: explain how to put this file in the correct location
        command1 = ["sudo ~/anki/drive-sdk/build/dist/bin/vehicle-tool --adapter=hci0 --device=" + mac1]
        command2 = ["sudo ~/anki/drive-sdk/build/dist/bin/vehicle-tool --adapter=hci0 --device=" + mac2]
        self.car1 = subprocess.Popen(command1, stdout = subprocess.PIPE, stdin = subprocess.PIPE, shell=TRUE)
        self.car2 = subprocess.Popen(command2, stdout = subprocess.PIPE, stdin = subprocess.PIPE, shell=TRUE)
        self.car1.communicate(input="connect")
        self.car2.communicate(input="connect")
        #For now, I have laneChangeSpeed and laneChangeAcceleration set as constants so that the trajectory
        #optimization has less variables to worry about
        self.laneChangeSpeed = laneChangeSpeed
        self.laneChangeAcceleration = laneChangeAcceleration


    #TODO: should we set a default acceleration?
    #Set the speed of the car
    #@param the car the speed change will be applied to
    #@param the speed to change the car to
    #@the acceleration at which to apply the change
    def setSpeed(car, speed, acceleration):
        car.communicate(input="set-speed " + speed " " + acceleration)
    
    #Shift lanes
    #PaperNote: must start in the left lane to keep track of what lane we are in
    #Change lanes
    #@param the car to send the command to
    #@param the lane change to be applied in integer form. Left is negative and right is possitive.
    def changeLane(car, laneChange):
        car.communicate(input="change-lane " + self.laneChangeSpeed + " " + self.laneChangeAcceleration + " " + laneChange)

    def get_car1():
        return self.car1

    def get_car2():
        return self.car2
