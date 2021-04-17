import classes
import copy
import threading, queue

# Checks if two banks have equal values
def checkBanksEqual(firstBank, secondBank):
    if (firstBank.chickens == secondBank.chickens and firstBank.wolves == secondBank.wolves and firstBank.boat == secondBank.boat):
        return True
    else:
        return False

# Checks if two states have equal configurations (disregards the list of previous actions)
def checkStatesEqual(firstState, secondState):
    if (checkBanksEqual(firstState.leftBank, secondState.leftBank) and checkBanksEqual(firstState.rightBank, secondState.rightBank)):
        return True
    else:
        return False


def checkNotExplored(added, newState):
    for i in added:
        if (checkStatesEqual(newState, i)):
            return False
    
    return True

def createNewState(action, currentState):
    newLeftBoat = not currentState.leftBank.boat
    currentChickens = currentWolves = oppositeChickens = oppositeWolves = newCurrentChickens = newCurrentWolves = newOppositeChickens = newOppositeWolves = newState = None

    if (currentState.leftBank.boat):
        currentChickens = currentState.leftBank.chickens
        currentWolves = currentState.leftBank.wolves 
        oppositeChickens = currentState.rightBank.chickens
        oppositeWolves = currentState.rightBank.wolves
    else:
        currentChickens = currentState.rightBank.chickens
        currentWolves = currentState.rightBank.wolves 
        oppositeChickens = currentState.leftBank.chickens
        oppositeWolves = currentState.leftBank.wolves

    if (action == 1):
        newCurrentChickens = currentChickens - 1
        newCurrentWolves = currentWolves
        newOppositeChickens = oppositeChickens + 1
        newOppositeWolves = oppositeWolves

    elif (action == 2):
        newCurrentChickens = currentChickens - 2
        newCurrentWolves = currentWolves
        newOppositeChickens = oppositeChickens + 2
        newOppositeWolves = oppositeWolves

    elif (action == 3):
        newCurrentChickens = currentChickens
        newCurrentWolves = currentWolves - 1
        newOppositeChickens = oppositeChickens
        newOppositeWolves = oppositeWolves + 1

    elif (action == 4):
        newCurrentChickens = currentChickens - 1
        newCurrentWolves = currentWolves - 1
        newOppositeChickens = oppositeChickens + 1
        newOppositeWolves = oppositeWolves + 1

    else:
        newCurrentChickens = currentChickens
        newCurrentWolves = currentWolves - 2
        newOppositeChickens = oppositeChickens
        newOppositeWolves = oppositeWolves + 2

    if (currentState.leftBank.boat):
        newState = classes.gameState(newCurrentChickens, newCurrentWolves, newLeftBoat, newOppositeChickens, newOppositeWolves, currentState.prevStates)
    else:
        newState = classes.gameState(newOppositeChickens, newOppositeWolves, newLeftBoat, newCurrentChickens, newCurrentWolves, currentState.prevStates)

    newState.prevStates.append(action)
    return newState

def expandNode(added, frontier, currentState, goalState = None):
    validActions = currentState.checkValidSuccessors()

    if (validActions[0]):
        newState = createNewState(1, currentState)

        if (checkNotExplored(added, newState)):
            added.append(newState)

            if (goalState != None):
                newHeuristic = abs(goalState.leftBank.chickens - newState.leftBank.chickens) + abs(goalState.rightBank.wolves - newState.rightBank.wolves) + 3 * len(newState.prevStates)
                frontier.put((newHeuristic, newState))
            else:
                frontier.put(newState)

    if (validActions[1]):
        newState = createNewState(2, currentState)

        if (checkNotExplored(added, newState)):
            added.append(newState)

            if (goalState != None):
                newHeuristic = abs(goalState.leftBank.chickens - newState.leftBank.chickens) + abs(goalState.rightBank.wolves - newState.rightBank.wolves) + 3 * len(newState.prevStates)
                frontier.put((newHeuristic, newState))
            else:
                frontier.put(newState)

    if (validActions[2]):
        newState = createNewState(3, currentState)

        if (checkNotExplored(added, newState)):
            added.append(newState)

            if (goalState != None):
                newHeuristic = abs(goalState.leftBank.chickens - newState.leftBank.chickens) + abs(goalState.rightBank.wolves - newState.rightBank.wolves) + 3 * len(newState.prevStates)
                frontier.put((newHeuristic, newState))
            else:
                frontier.put(newState)    

    if (validActions[3]):
        newState = createNewState(4, currentState)

        if (checkNotExplored(added, newState)):
            added.append(newState)
            
            if (goalState != None):
                newHeuristic = abs(goalState.leftBank.chickens - newState.leftBank.chickens) + abs(goalState.rightBank.wolves - newState.rightBank.wolves) + 3 * len(newState.prevStates)
                frontier.put((newHeuristic, newState))
            else:
                frontier.put(newState) 
                    
    if (validActions[4]):
        newState = createNewState(5, currentState)

        if (checkNotExplored(added, newState)):
            added.append(newState)
            
            if (goalState != None):
                newHeuristic = abs(goalState.leftBank.chickens - newState.leftBank.chickens) + abs(goalState.rightBank.wolves - newState.rightBank.wolves) + 3 * len(newState.prevStates)
                frontier.put((newHeuristic, newState))
            else:
                frontier.put(newState) 
    return added, frontier