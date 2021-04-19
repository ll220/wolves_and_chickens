import classes
import functions 
import threading, queue

class astarGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, lcg, lwg, lbg, rcg, rwg)

        self.frontier = queue.PriorityQueue()
        self.initialHeuristic = abs(self.basics.goalState.leftBank.chickens - self.basics.initialState.leftBank.chickens) + abs(self.basics.goalState.rightBank.wolves - self.basics.initialState.rightBank.wolves)
        self.frontier.put((self.initialHeuristic, self.basics.initialState))


    def playGame(self):
        while(not self.frontier.empty()):

            newNode = self.frontier.get()
            currentState = newNode[1]

            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount
            else:       
                 currentState.print() 
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState, self.basics.goalState)
        
        return None

# newGame = astarGame(3, 3, 1, 0, 0, 0, 0, 0, 3, 3)
# finalState, number = newGame.playGame()

# finalState.print()
# print("Expanded: ", number)