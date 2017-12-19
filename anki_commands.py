import subprocess
import shlex
# TODO: make this more extensible, so n cars could be used
#
"""
    This class allows the computer to communicate with the Anki vehicles using
    the subprocess library. We wrote it as a class in order to retain the ability
    to instantiate it with various vehicles as well as alter the hyper parameters
    laneChangeSpeed and laneChangeAcceleration.

"""
class anki_commands:
    """
    Anki encapsulates the commands to communicate with the vehicle.
    """
    #instantiates the c programs the communicate with the cars
    def __init__(carsMacs, mac1, mac2, laneChangeSpeed, laneChangeAcceleration):
        # PaperNote: explain how to put this file in the correct location
        """
        Construct a new Anki object.

        param carsMacs: An array of the mac addresses for each vehicle. Instructions
        for finding these can be found within the Anki set up documentation.

        param laneChangeSpeed: This is a hyper parameter that determines
        the velocity along the X axis at which the car changes lanes.

        param laneChangeAcceleration: This is the acceleration to laneChangeSpeed
        and is another hyper parameter.

        return: This function returns nothing.
        """
        command1 = ["~/anki/drive-sdk/build/dist/bin/vehicle-tool --adapter=hci0 --device=" + carsMacs[0]]
        command2 = ["~/anki/drive-sdk/build/dist/bin/vehicle-tool --adapter=hci0 --device=" + carsMacs[1]]
        self.car1 = subprocess.Popen(command1, stdout = subprocess.PIPE, stdin = subprocess.PIPE, shell=TRUE)
        self.car2 = subprocess.Popen(command2, stdout = subprocess.PIPE, stdin = subprocess.PIPE, shell=TRUE)
        self.car1.communicate(input="connect")
        self.car2.communicate(input="connect")
        #For now, I have laneChangeSpeed and laneChangeAcceleration set as constants so that the trajectory
        #optimization has less variables to worry about
        self.laneChangeSpeed = laneChangeSpeed
        self.laneChangeAcceleration = laneChangeAcceleration


    #TODO: should we set a default acceleration?

    def setSpeed(car, speed, acceleration):
        """
        Set the speed of the vehicle.


        param car: The car the speed change will be applied to. This can be acquired
        through functions get_car1() or get_car2()

        param speed: The speed to change the car to

        param acceleration: The acceleration at which to apply the change

        return: This function does not return anything
        """
        car.communicate(input="set-speed " + speed + " " + acceleration)

    # PaperNote: must start in the left lane to keep track of what lane we are in


    def changeLane(car, laneChange):
        """
        changeLane sends a shift lanes command to the designated vehicle.

        param car: The car to send the command to, acquired with this.get_car1()
        or this.get_car2()

        param laneChange: The lane change to be applied in integer form.
        Left is negative and right is possitive.

        return: This function returns nothing.
        """
        car.communicate(input="change-lane " + self.laneChangeSpeed + " " + self.laneChangeAcceleration + " " + laneChange)



    def get_car1():
        """
        Acquire the subprocess to communicate with car1.

        return: This returns the subprocess object used to communicate with car1.
        """
        return self.car1


    def get_car2():
        """
        Acquire the subprocess to communicate with car2.

        return: This returns the subprocess object used to communicate with car2.
        """
        return self.car2
