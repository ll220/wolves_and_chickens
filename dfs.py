import classes
import functions
import threading, queue

class dfsGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg)

        self.frontier = queue.LifoQueue()
        self.frontier.put(self.basics.initialState)


    def playGame(self):
        while(not self.frontier.empty()):
            currentState = self.frontier.get()

            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount
            else:        
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState)
        
        return None




# newGame = dfsGame(0, 0, 0, 96, 94, 96, 94, 1, 0, 0)

# finalState, number = newGame.playGame()

# finalState.print()
# print("Expanded: ", number)
# print(len(finalState.prevStates))
