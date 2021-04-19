import classes
import functions
import threading, queue

# A class that carries out a depth first search of the wolves and chickens game given an initial state and a goal state
class dfsGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg)

        self.frontier = queue.LifoQueue()   # Using a LIFO queue
        self.frontier.put(self.basics.initialState)

    # Carries out playing of the game using a depth first search
    def playGame(self):
        # Continuously expand nodes until the frontier is empty
        while(not self.frontier.empty()):
            currentState = self.frontier.get()

            # If a goal node is found, return the final state and the expanded count
            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount
            # Otherwise, expand the node
            else:        
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState)
        
        # If the frontier is empty before a goal node is found, return None
        return None




# newGame = dfsGame(0, 0, 0, 96, 94, 96, 94, 1, 0, 0)

# finalState, number = newGame.playGame()

# finalState.print()
# print("Expanded: ", number)
# print(len(finalState.prevStates))
