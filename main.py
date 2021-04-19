import bfs
import dfs
import iddfs
import astar
import classes
import functions
import sys
import numpy as np


# Takes arguments from the command line and reads in an initial state and a goal state from files. Does not have error checking 
# in the cases where the file names do not exist and the order of arguments. Also does not include error checking for if the initial states are valid or not. 
# Prints the solution path to an output file whose name is designated by the user along with the type of search, the number of actions
# performed on the states to reach the goal node, and the number of nodes expanded. 
class totalGame():
    def __init__(self, startFileInput, goalFileInput, modeInput, outputFileInput):
        self.mode = modeInput
        self.outputFile = outputFileInput

        self.lcs = int(startFileInput[0, 0])
        self.lws = int(startFileInput[0, 1])
        self.lbs = int(startFileInput[0, 2])
        self.rcs = int(startFileInput[1, 0])
        self.rws = int(startFileInput[1, 1])
        self.rbs = int(startFileInput[1, 2])
        
        self.lcg = int(goalFileInput[0, 0])
        self.lwg = int(goalFileInput[0, 1])
        self.lbg = int(goalFileInput[0, 2])
        self.rcg = int(goalFileInput[1, 0])
        self.rwg = int(goalFileInput[1, 1])
        self.rbg = int(goalFileInput[1, 2])

    # Carries out the search depending on the user's specifications. Returns the initial state, goal state, and mode and result
    def playTotalGame(self):
        result = game = None
        initialState = classes.gameState(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.rbs)

        if (mode == "bfs"):
            game = bfs.bfsGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.rbs, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg, self.rbg)
        elif(mode == "dfs"):
            game = dfs.dfsGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.rbs, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg, self.rbg)
        elif(mode == "iddfs"):
            game = iddfs.iddfsGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.rbs, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg, self.rbg)
        elif(mode == "astar"):
            game = astar.astarGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.rbs, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg, self.rbg)

        result = game.playGame()
        return initialState, result, self.outputFile

# Takes in a list of arguments from command line, parses them, and reads the content of the files into numpy arrays to be input into the totalGame class  
def getFileInput(commandLineArguments):
    if (len(sys.argv) != 5):
        print("Please input all arguments when starting program")   # A little error checking for if the user input enough arguments
        quit()
    else:
        startFileInput = np.loadtxt(commandLineArguments[1], delimiter = ",")   # Read in values from the initial state file
        goalFileInput = np.loadtxt(commandLineArguments[2], delimiter=",")  # Read in values from the goal state file
        mode = commandLineArguments[3]  # Get the mode
        outputFileInput = commandLineArguments[4]   # Get the output file name

    # Returns the reformatted values 
    return startFileInput, goalFileInput, mode, outputFileInput 

# Takes the result from the search and prints it to an output file that the user specifies
def printGameResults(initialState, result, outputFile):
    # Open the file for writing in
    f = open(outputFile, "w")    
    
    # Print no solution found if a path to the goal node was not found
    if (result == None):
        f.write("No solution found")
    else:
        expanded = result[1]
        actions = result[0].prevStates
        currentState = initialState

        # At the top of the file, print number of nodes expanded, the mode, and the path length of the solution path (number of actions performed)
        header = "Mode: " + str(mode) + "\t" + "Expanded: " + str(expanded) + "\t" + "Number of Actions: " + str(len(actions)) + "\n" + "\n" + "Solution Path: " + "\n" + "\n"
        f.write(header)

        # Print the initial state
        f.write("Left -- " + "Chickens: " + str(currentState.leftBank.chickens) + "\t" + " Wolves: " + str(currentState.leftBank.wolves) + "\t" + " Boat: " + str(currentState.leftBank.boat) + "\n")
        f.write("Right -- " + "Chickens: " + str(currentState.rightBank.chickens) + "\t" + " Wolves: " + str(currentState.rightBank.wolves) + "\t" + " Boat: " + str(currentState.rightBank.boat) + "\n")
        f.write("\n")

        # Print out all the states encountered along the solution path
        for i in actions:
            currentState = functions.createNewState(i, currentState)
            f.write("Left -- " + "Chickens: " + str(currentState.leftBank.chickens) + "\t" + " Wolves: " + str(currentState.leftBank.wolves) + "\t" + " Boat: " + str(currentState.leftBank.boat) + "\n")
            f.write("Right -- " + "Chickens: " + str(currentState.rightBank.chickens) + "\t" + " Wolves: " + str(currentState.rightBank.wolves) + "\t" + " Boat: " + str(currentState.rightBank.boat) + "\n")
            f.write("\n")

    # Print out the contents of the file to the command line
    f.close()
    f = open(outputFile, "r")
    print(f.read())
    f.close()


startFileInput, goalFileInput, mode, outputFileInput = getFileInput(sys.argv)   # Get the commmand line arguments and data from the external files
game = totalGame(startFileInput, goalFileInput, mode, outputFileInput)  # Create a new game object 
initialState, result, outputFile = game.playTotalGame() # Carry out the search
printGameResults(initialState, result, outputFile)  # Print the results to an output file and to the command line

