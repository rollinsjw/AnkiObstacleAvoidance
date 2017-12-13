import subprocess
import shlex
# p = subprocess
# p.Popen(['git commit', '-m', "' hello"], shell=True)
# p.Popen(['echo "hello"'], creationflags=1, shell=True)
# process = subprocess.Popen(
#     shlex.split(""" echo 'hello' """))
# process.wait()
# print (process.returncode)


# def setSpeed(command):
#     subprocess.call(command)
# def setAccel(desiredAccel):
#     subprocess.call()
#
#     Popen.communicate(input=None)
# Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument should be a string to be sent to the child process, or None, if no data should be sent to the child.
#
#
#solution:
#This launches a new terminal, we can then find the prcoess ID in ordre to send it new inputs while the program is running
# subprocess.call(['gnome-terminal', '-x', 'python bb.py'])


#ideas:
#create a subprocess and communicate with it
#open a gnome terminal
#write a c script for each possible optional
#   each script connects with the car and sends it a command
#    Do I need to connect with it? or can I just send it commands
#
class Anki:

    #instantiates the c programs the communicate with the cars
    def __init__(carsMacs):


    #TODO: should we set a default acceleration?
    def setSpeed(speed, acceleration):

    def changeLane(lane):f
