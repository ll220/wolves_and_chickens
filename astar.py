import classes
import functions 
import threading, queue

# Carries out a graph search astar search for the wolves and chickens game given an initial and a goal state
# h(n) is the sum of the absolute value of the difference between the goal left bank's and the current state's left bank's chickens and wolves. 
# Boats are not included in the heuristic. The path to each node, each state, or the cost of each trip across the river is three to ensure the 
# heuristic is consistent. Tiebreaking always favors the node that was added first.
class astarGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg)

        self.frontier = queue.PriorityQueue()   # Using a priority queue

        # Elements of the priority queue are tuples that are (f(n), state)
        self.initialHeuristic = abs(self.basics.goalState.leftBank.chickens - self.basics.initialState.leftBank.chickens) + abs(self.basics.goalState.rightBank.wolves - self.basics.initialState.rightBank.wolves)
        self.frontier.put((self.initialHeuristic, self.basics.initialState))

    # Carries out the a star search. Similar to bfs except that a priority queue is used to order elements
    def playGame(self):
        while(not self.frontier.empty()):

            newNode = self.frontier.get()
            currentState = newNode[1]

            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount
            else:       
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState, self.basics.goalState)
        
        return None

# newGame = astarGame(0, 0, 0, 96, 94, 96, 94, 1, 0, 0)
# finalState, number = newGame.playGame()

# finalState.print()
# print("Expanded: ", number)