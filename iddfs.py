import classes
import functions 
import threading, queue

# A class that carries out iterative deepening depth first search of a wolves and chickens game given an initial and a goal state
# This search does not include a maxmimum depth cutoff in which the program terminates at for all games. It instead keeps track 
# of whether or not the search tree terminates before the cutoff is reached, therefore it will always find a goal node if a goal node exists
# and if a goal node does not exist, then it will be able to tell if the cutoff reaches a greater value than the maximum depth of the search tree
class iddfsGame(classes.gameBasics):
    def __init__(self, lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg):
        self.basics = classes.gameBasics(lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg)

        self.frontier = queue.LifoQueue()   # Using a LIFO queue
        self.frontier.put(self.basics.initialState)     # Add the first state to the frontier
        self.depthLimit = 0     # Keep track of the depth limit that continuously increments

        # Keep track of the maximum depth of the search tree. If the end of the search tree is encountered before 
        # the maximum depth of the current search is encountered, then a solution path does not exist
        self.maxDepth = 0       


    # Carries out a single depth first search with a given max depth. Returns none 
    def limitedDFS(self):

        # Continuously expand nodes while the frontier is not empty
        while(not self.frontier.empty()):
            currentState = self.frontier.get()

            # Keep track of whether or not the search tree has reached its limit before the max depth is reached 
            self.maxDepth = max(self.maxDepth, len(currentState.prevStates))

            # Return the expanded count and the final state if a goal node is found
            if (functions.checkStatesEqual(currentState, self.basics.goalState)):
                return currentState, self.basics.expandedCount

            # Expand the node if the node is not at the cutoff depth for the current search
            elif(len(currentState.prevStates) < self.depthLimit):        
                 self.basics.expandedCount = self.basics.expandedCount + 1
                 self.basics.added, self.frontier = functions.expandNode(self.basics.added, self.frontier, currentState)
        
        # Clear the explored list for future searches
        self.basics.added.clear()
        return None # Return None if a goal node is not found before encountering the depth limit

    # Carries out the playing of the iddfs
    def playGame(self):
        while (True):

            # This program takes a long time with larger values. This is to ensure that the program is running properly when calculating large values
            print("Now searching with depth: ", self.depthLimit)
            result = self.limitedDFS()

            # If the goal node is encountered in one of the searches, return the result
            if (result != None):
                return result

            # Otherwise if the max depth of the tree has not been encountered yet, then increment the cutoff by one and search again
            elif(self.maxDepth == self.depthLimit):
                self.frontier.put(self.basics.initialState)     # Reset the frontier
                self.depthLimit = self.depthLimit + 1

            # Otherwise, if a goal node is not found and the entire search tree has been generated, then return None
            else:
                return None


# newGame = iddfsGame(0, 0, 0, 96, 94, 96, 94, 1, 0, 0)
# result = newGame.playGame()
# if (result == None):
#     print(result)
# else:
#     result[0].print()
#     print("Expanded: ", result[1])
