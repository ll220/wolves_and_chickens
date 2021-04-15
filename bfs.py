import classes
import threading, queue

class bfsGame(classes.gameState):
    def __init__(self, lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg):
        self.initialState = classes.gameState(lcs, lws, lbs, rcs, rws)
        self.goalState = classes.gameState(lcg, lwg, lbg, rcg, rwg)

        self.frontier = queue.Queue()
        self.frontier.put(self.initialState)

        self.added = [self.initialState]
        self.expandedCount = 0

    def checkNotExplored(self, newState):
        for i in self.added:
            if (classes.checkStatesEqual(newState, i)):
                return False
        
        return True

    def expandNode(self, currentState):
        validActions = currentState.checkValidSuccessors()

        if (currentState.leftBank.boat):
            if (validActions[0]):
                newState = createNewStateLeft(1, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)

            if (validActions[1]):
                newState = createNewStateLeft(2, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)

            if (validActions[2]):
                newState = createNewStateLeft(3, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)    

            if (validActions[3]):
                newState = createNewStateLeft(4, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)  
            
            if (validActions[4]):
                newState = createNewStateLeft(5, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)  

        else: 
            if (validActions[0]):
                newState = createNewStateRight(1, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)

            if (validActions[1]):
                newState = createNewStateRight(2, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)

            if (validActions[2]):
                newState = createNewStateRight(3, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)    

            if (validActions[3]):
                newState = createNewStateRight(4, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)  
            
            if (validActions[4]):
                newState = createNewStateRight(5, currentState)

                if (self.checkNotExplored(newState)):
                    self.added.append(newState)
                    self.frontier.put(newState)  
        


    def playGame(self):
        while(not self.frontier.empty()):
            currentState = self.frontier.get()

            if (classes.checkStatesEqual(currentState, self.goalState)):
                return currentState, self.expandedCount
            else:           
                 self.expandedCount = self.expandedCount + 1
                 self.expandNode(currentState)
        
        return None


def createNewStateLeft(mode, currentState):
    newLeftBoat = not currentState.leftBank.boat
    newLeftChickens = newLeftWolves = newRightChicken = newRightWolves = newState = None

    if (mode == 1):
        newLeftChickens = currentState.leftBank.chickens - 1
        newLeftWolves = currentState.leftBank.wolves 
        newRightChicken = currentState.rightBank.chickens + 1
        newRightWolves = currentState.rightBank.wolves


    elif (mode == 2):
        newLeftChickens = currentState.leftBank.chickens - 2
        newLeftWolves = currentState.leftBank.wolves 
        newRightChicken = currentState.rightBank.chickens + 2
        newRightWolves = currentState.rightBank.wolves

    elif (mode == 3):
        newLeftChickens = currentState.leftBank.chickens
        newLeftWolves = currentState.leftBank.wolves - 1
        newRightChicken = currentState.rightBank.chickens
        newRightWolves = currentState.rightBank.wolves + 1

    elif (mode == 4):
        newLeftChickens = currentState.leftBank.chickens - 1
        newLeftWolves = currentState.leftBank.wolves - 1
        newRightChicken = currentState.rightBank.chickens + 1
        newRightWolves = currentState.rightBank.wolves + 1

    elif (mode == 5):
        newLeftChickens = currentState.leftBank.chickens 
        newLeftWolves = currentState.leftBank.wolves - 2
        newRightChicken = currentState.rightBank.chickens
        newRightWolves = currentState.rightBank.wolves + 2

    newState = classes.gameState(newLeftChickens, newLeftWolves, newLeftBoat, newRightChicken, newRightWolves, currentState.prevStates)
    newState.prevStates.insert(0, mode)
    return newState

def createNewStateRight(mode, currentState):
    newLeftBoat = not currentState.leftBank.boat
    newLeftChickens = newLeftWolves = newRightChicken = newRightWolves = newState = None

    if (mode == 1):
        newLeftChickens = currentState.leftBank.chickens + 1
        newLeftWolves = currentState.leftBank.wolves 
        newRightChicken = currentState.rightBank.chickens - 1
        newRightWolves = currentState.rightBank.wolves


    elif (mode == 2):
        newLeftChickens = currentState.leftBank.chickens + 2
        newLeftWolves = currentState.leftBank.wolves 
        newRightChicken = currentState.rightBank.chickens - 2
        newRightWolves = currentState.rightBank.wolves

    elif (mode == 3):
        newLeftChickens = currentState.leftBank.chickens
        newLeftWolves = currentState.leftBank.wolves + 1
        newRightChicken = currentState.rightBank.chickens
        newRightWolves = currentState.rightBank.wolves - 1

    elif (mode == 4):
        newLeftChickens = currentState.leftBank.chickens + 1
        newLeftWolves = currentState.leftBank.wolves + 1
        newRightChicken = currentState.rightBank.chickens - 1
        newRightWolves = currentState.rightBank.wolves - 1

    elif (mode == 5):
        newLeftChickens = currentState.leftBank.chickens 
        newLeftWolves = currentState.leftBank.wolves + 2
        newRightChicken = currentState.rightBank.chickens
        newRightWolves = currentState.rightBank.wolves - 2

    newState = classes.gameState(newLeftChickens, newLeftWolves, newLeftBoat, newRightChicken, newRightWolves, currentState.prevStates)
    newState.prevStates.insert(0, mode)
    return newState
    

newGame = bfsGame(3, 3, 1, 0, 0, 0, 0, 0, 3, 3)

finalState, number = newGame.playGame()

finalState.print()

