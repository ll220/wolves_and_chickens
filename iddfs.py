import classes
import functions 
import threading, queue

class iddfsGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg)

        self.frontier = queue.LifoQueue()
        self.frontier.put(self.basics.initialState)
        self.depthLimit = 0
        self.maxDepth = 0

    def limitedDFS(self):
        while(not self.frontier.empty()):
            currentState = self.frontier.get()
            self.maxDepth = max(self.maxDepth, len(currentState.prevStates))
            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount

            elif(len(currentState.prevStates) < self.depthLimit):        
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState)
        
        self.basics.added.clear()
        return None

    def playGame(self):
        while (True):
            print(self.depthLimit)
            result = self.limitedDFS()

            if (result != None):
                return result
            elif(self.maxDepth == self.depthLimit):
                self.frontier.put(self.basics.initialState)
                self.depthLimit = self.depthLimit + 1
            else:
                return None


newGame = iddfsGame(0, 0, 0, 96, 94, 96, 94, 1, 0, 0)
result = newGame.playGame()
if (result == None):
    print(result)
else:
    result[0].print()
    print("Expanded: ", result[1])
