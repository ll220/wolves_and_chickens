import bfs
import dfs
import iddfs
import astar
import classes
import functions
import sys
import numpy as np

class totalGame():
    def __init__(self, startFileInput, goalFileInput, modeInput, outputFileInput):
        self.mode = modeInput
        self.outputFile = outputFileInput

        self.lcs = int(startFileInput[0, 0])
        self.lws = int(startFileInput[0, 1])
        self.lbs = int(startFileInput[0, 2])
        self.rcs = int(startFileInput[1, 0])
        self.rws = int(startFileInput[1, 1])
        
        self.lcg = int(goalFileInput[0, 0])
        self.lwg = int(goalFileInput[0, 1])
        self.lbg = int(goalFileInput[0, 2])
        self.rcg = int(goalFileInput[1, 0])
        self.rwg = int(goalFileInput[1, 1])

    def playTotalGame(self):
        result = game = None
        initialState = classes.gameState(self.lcs, self.lws, self.lbs, self.rcs, self.rws)

        if (mode == "bfs"):
            game = bfs.bfsGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg)
        elif(mode == "dfs"):
            game = dfs.dfsGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg)
        elif(mode == "iddfs"):
            game = iddfs.iddfsGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg)
        elif(mode == "astar"):
            game = astar.astarGame(self.lcs, self.lws, self.lbs, self.rcs, self.rws, self.lcg, self.lwg, self.lbg, self.rcg, self.rwg)

        result = game.playGame()
        return initialState, result, self.outputFile
         
def getFileInput(commandLineArguments):
    if (len(sys.argv) != 5):
        print("Please input all arguments when starting program")
    else:
        startFileInput = np.loadtxt(commandLineArguments[1], delimiter = ",")
        goalFileInput = np.loadtxt(commandLineArguments[2], delimiter=",")
        mode = commandLineArguments[3]
        outputFileInput = commandLineArguments[4]

    return startFileInput, goalFileInput, mode, outputFileInput

def printGameResults(initialState, result, outputFile):
    f = open(outputFile, "w")    
    
    if (result == None):
        f.write("No solution found")
    else:
        expanded = result[1]
        actions = result[0].prevStates
        currentState = initialState

        header = "Mode: " + str(mode) + "\t" + "Expanded: " + str(expanded) + "\t" + "Number of Actions: " + str(len(actions)) + "\n" + "\n" + "Solution Path: " + "\n" + "\n"
        f.write(header)

        f.write("Left -- " + "Chickens: " + str(currentState.leftBank.chickens) + "\t" + " Wolves: " + str(currentState.leftBank.wolves) + "\t" + " Boat: " + str(currentState.leftBank.boat) + "\n")
        f.write("Right -- " + "Chickens: " + str(currentState.rightBank.chickens) + "\t" + " Wolves: " + str(currentState.rightBank.wolves) + "\t" + " Boat: " + str(currentState.rightBank.boat) + "\n")
        f.write("\n")

        for i in actions:
            currentState = functions.createNewState(i, currentState)
            f.write("Left -- " + "Chickens: " + str(currentState.leftBank.chickens) + "\t" + " Wolves: " + str(currentState.leftBank.wolves) + "\t" + " Boat: " + str(currentState.leftBank.boat) + "\n")
            f.write("Right -- " + "Chickens: " + str(currentState.rightBank.chickens) + "\t" + " Wolves: " + str(currentState.rightBank.wolves) + "\t" + " Boat: " + str(currentState.rightBank.boat) + "\n")
            f.write("\n")

        f.close()
        f = open(outputFile, "r")
        print(f.read())
        f.close()


startFileInput, goalFileInput, mode, outputFileInput = getFileInput(sys.argv)
game = totalGame(startFileInput, goalFileInput, mode, outputFileInput)
initialState, result, outputFile = game.playTotalGame()
printGameResults(initialState, result, outputFile)

