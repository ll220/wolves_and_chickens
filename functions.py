import classes
import copy
import threading, queue

##############################################################################################################################################
# Includes functions that reoccur in all searche types. Include functions that will expand nodes and add them to a frontier, 
# functions that will create a new state based on an action performed on a previous node, and checking a node against a list of explored nodes.
###############################################################################################################################################


####################################################################
# Actions are encoded as: 
#     1: Send one chicken across
#     2: Send two chickens across
#     3: Send one wolf across
#     4: Send one wolf and one chicken across
#     5: Send two wolves across
####################################################################

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

# Checks a state against a list of explored states and returns whether or not it exists in it
def checkNotExplored(added, newState):
    for i in added:
        if (checkStatesEqual(newState, i)):
            return False
    
    return True

# Creates a new state that represents the result of an action performed on a previous state. Actions are encoded as above
def createNewState(action, currentState):
    newLeftBoat = newRightBoat = 0

    # Switches the boat to the opposite side
    if (currentState.leftBank.boat == 1):
        newLeftBoat = 0
        newRightBoat = 1
    else:
        newLeftBoat = 1
        newRightBoat = 0

    currentChickens = currentWolves = oppositeChickens = oppositeWolves = newCurrentChickens = newCurrentWolves = newOppositeChickens = newOppositeWolves = newState = None

    # Current side = the side the boat originally was on before being switched over
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

    # Change the values for chickens and wolves for each side based on the action
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

    # Create the state
    if (currentState.leftBank.boat):
        newState = classes.gameState(newCurrentChickens, newCurrentWolves, newLeftBoat, newOppositeChickens, newOppositeWolves, newRightBoat, currentState.prevStates)
    else:
        newState = classes.gameState(newOppositeChickens, newOppositeWolves, newLeftBoat, newCurrentChickens, newCurrentWolves, newRightBoat, currentState.prevStates)

    # Append the action to the list of previous states
    newState.prevStates.append(action)
    return newState

# Takes a node and a frontier and an explored list and expands the node.
# goalState is input as an argument if astar search is being used. This is to calculate the heuristic for the new nodes by comparing their values 
# to the goal state
def expandNode(added, frontier, currentState, goalState = None):

    # Check for all valid actions
    validActions = currentState.checkValidSuccessors()

    # Create a new state for every action that can be performed on the node. Add it if has not been explored before
    if (validActions[0]):
        newState = createNewState(1, currentState)

        if (checkNotExplored(added, newState)):
            added.append(newState)

            if (goalState != None):
                # If a goal state is input (aka if astar search is being used), calculate the heuristic and add to the queue as a tuple
                newHeuristic = abs(goalState.leftBank.chickens - newState.leftBank.chickens) + abs(goalState.rightBank.wolves - newState.rightBank.wolves) + 3 * len(newState.prevStates)
                frontier.put((newHeuristic, newState))
            else:
                # Otherwise, just add the new state
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