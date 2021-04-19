import classes
import functions
import threading, queue

# A class that carries out a breadth first search of the wolves and chickens game given an initial and goal state
class bfsGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg)

        self.frontier = queue.Queue()   # Using a FIFO queue
        self.frontier.put(self.basics.initialState) # Put the initial state on the frontier


    # Carries out playing of game
    def playGame(self):
        # Repeatedly expand nodes until the frontier is empty
        while(not self.frontier.empty()):
            currentState = self.frontier.get()

            # If a goal node is found, return the expanded count and the final state
            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount
            # Otherwise, expand the node
            else:        
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState)
        
        # If a solution is not found before the frontier becomes empty, return None
        return None




# newGame = bfsGame(96, 94, 1, 0, 0, 0, 0, 0, 96, 94)

# finalState, number = newGame.playGame()

# finalState.print()
# print("Expanded: ", number)
# print(len(finalState.prevStates))

