#############################################################################################################################################
# Includes classes for banks and states and functions that allows the user to determine valid actions based off of state configuration 
# Also includes a class for elements that are reoccuring in all search types, ie the initial state, goal state, explored nodes and expanded count
#############################################################################################################################################

import copy
import Queue

####################################################################
# Actions are encoded as: 
#     1: Send one chicken across
#     2: Send two chickens across
#     3: Send one wolf across
#     4: Send one wolf and one chicken across
#     5: Send two wolves across
####################################################################

# Represents each bank that exists in each state. Contains number of boats, chickens and wolves 
class bank: 
    def __init__(self, c, w, b):
        self.chickens = c
        self.wolves = w
        self.boat = b

    # Prints out values from a bank including chickens, wolves, and boat
    def bankPrint(self):
       print("Chickens: ", self.chickens, " Wolves: ", self.wolves, " Boat: ", self.boat)

# Represents each state, contains a list that contains previous states as previous actions encoded with integers
class gameState(bank): 
    def __init__(self, c_left, w_left, boat_left, c_right, w_right, boat_right, prev = []): 
        self.leftBank = bank(c_left, w_left, boat_left)
        self.rightBank = bank(c_right, w_right, boat_right)
        self.prevStates = copy.deepcopy(prev)

    # For astar search. This is used for comparison if a new node has an equal heuristic to a node in the priority queue. Favors the node added first for FIFO functionality
    def __lt__(self, other):
        return False

    # Returns a list of five Booleans. Each of them represents actions: [1, 2, 3, 4, 5]. True indicates if the next valid and a successor can be generated via that action
    def checkValidSuccessors (self): 
        validActions = [False, False, False, False, False]

        if (self.leftBank.boat):   # Check possible actions moving right, assuming the banks are in a valid state
            # Check if the left bank has chickens to send
            if (self.leftBank.chickens > 0):
                # You can have more wolves than chickens on the left if there are no chickens, else check if sending one chicken does not violate conditions 
                if (self.rightBank.wolves <= self.rightBank.chickens + 1 and (self.leftBank.chickens == 1 or self.leftBank.wolves <= self.leftBank.chickens - 1)):
                    validActions[0] = True 
                # If two chickens can be sent, if conditions are not violated on the left and does not violate conditions for right
                if (self.leftBank.chickens >= 2 and self.rightBank.wolves <= self.rightBank.chickens + 2 and (self.leftBank.chickens - 2 == 0 or self.leftBank.wolves <= self.leftBank.chickens - 2)):
                    validActions[1] = True 
                # If there are wolves on the left side and if wolves <= chickens on the right side (there could be some wolves but no chickens)
                if (self.leftBank.wolves > 0 and self.rightBank.wolves <= self.rightBank.chickens): 
                    validActions[3] = True

            # Check if the left bank has wolves to send
            if (self.leftBank.wolves > 0):
                # Can send any number of wolves over if there are no chickens on the right side, else, check if adding wolf to the right side doesn't violate conditions
                if (self.rightBank.chickens == 0 or self.rightBank.wolves + 1 <= self.rightBank.chickens): 
                    validActions[2] = True
                # If there are two wolves to send and again, checking if no chickens or if adding 2 wolves will violate right side
                if (self.leftBank.wolves >= 2 and (self.rightBank.chickens == 0 or (self.rightBank.wolves + 2 <= self.rightBank.chickens))): 
                    validActions[4] = True

        else: 
            if (self.rightBank.chickens > 0):
                # Check if can send one chicken over to left 
                if (self.leftBank.wolves <= self.leftBank.chickens + 1 and (self.rightBank.chickens == 1 or self.rightBank.wolves <= self.rightBank.chickens - 1)):
                    validActions[0] = True 
                # Check if two chickens can be sent to the left
                if (self.rightBank.chickens >= 2 and self.leftBank.wolves <= self.leftBank.chickens + 2 and (self.rightBank.chickens == 2 or self.rightBank.wolves <= self.rightBank.chickens - 2)):
                    validActions[1] = True 
                # Check if a wolf and chicken can be sent to the left
                if (self.rightBank.wolves > 0 and self.leftBank.wolves <= self.leftBank.chickens): 
                    validActions[3] = True

            # Check if the right bank has wolves to send
            if (self.rightBank.wolves > 0):
                # Check if can send one wolf over
                if (self.leftBank.chickens == 0 or self.leftBank.wolves + 1 <= self.leftBank.chickens): 
                    validActions[2] = True
                # Check if two wolves can be sent over left
                if (self.rightBank.wolves >= 2 and (self.leftBank.chickens == 0 or (self.leftBank.wolves + 2 <= self.leftBank.chickens))): 
                    validActions[4] = True
        return validActions

    # Prints out values from a state, including values from left and right banks and the list of previous states
    def statePrint(self):
        print("Left -- ")
        self.leftBank.bankPrint()
        print("Right -- ")
        self.rightBank.bankPrint()

        print("Prev states:")
        for i in (self.prevStates):
            print(i)

        print("\n")

# A class that contains elements that occur in every search type, such as initial state, goal state, and explored list and expanded count
class gameBasics (gameState): 
    def __init__(self, lcs, lws, lbs, rcs, rws, rbs, lcg, lwg, lbg, rcg, rwg, rbg):
        self.initialState = gameState(lcs, lws, lbs, rcs, rws, rbs)
        self.goalState = gameState(lcg, lwg, lbg, rcg, rwg, rbg)

        self.added = [self.initialState]
        self.expandedCount = 0

