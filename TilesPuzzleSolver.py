import math, random

class puzzle:
    def __init__(self):
        self.InitialState = ['1','2','3','4','5','6','7','8','-']
        self.GoalState = ['1','2','3','4','5','6','7','8','-']
        self.PreviousStates = []
        self.SmallestDistanceStates = []

        
    def shuffler(self):
        while True:
            tiles =[]
            tiles = self.InitialState
            tilesState = []
            place = random.randint(1,4)  #becuase of randomally swap 2 no.'s
            getEmptyPlace = tiles.index('-')+1
            tilesState.extend(tiles)
            movingPlaces = self.movingBoundries(getEmptyPlace)
            
            if getEmptyPlace+3 <= 9 and place == 1:
                temp = tilesState[tiles.index('-')]
                tilesState[tiles.index('-')] = tilesState[tiles.index('-')+3]
                tilesState[tiles.index('-')+3] = temp
                self.InitialState = tilesState
                return

            elif getEmptyPlace-3 >= 1 and place == 2:
                temp = tilesState[tiles.index('-')]
                tilesState[tiles.index('-')] = tilesState[tiles.index('-')-3]
                tilesState[tiles.index('-')-3] = temp
                self.InitialState = tilesState
                return

            elif getEmptyPlace-1 >= movingPlaces[0] and place == 3:
                temp = tilesState[tiles.index('-')]
                tilesState[tiles.index('-')] = tilesState[tiles.index('-')-1]
                tilesState[tiles.index('-')-1] = temp
                self.InitialState = tilesState
                return

            elif getEmptyPlace+1 <= movingPlaces[1] and place == 4:
                temp = tilesState[tiles.index('-')]
                tilesState[tiles.index('-')] = tilesState[tiles.index('-')+1]
                tilesState[tiles.index('-')+1] = temp
                self.InitialState = tilesState
                return


    def movingBoundries(self, emptyPlace):
        tilePuzzleList = [[1,2,3], [4,5,6], [7,8,9]]
        first = 0
        last = 0

        for tile in tilePuzzleList:
            if emptyPlace in tile:
                first = tile[0]
                last = tile[2]

        return [first, last]


    def getNextState(self):
        nextState = []
        minCostTileState = []

        while True:
            heuristicCost = 100
            for hrCostState in self.SmallestDistanceStates:
                if(hrCostState[-1] < heuristicCost):
                    heuristicCost = hrCostState[-1]
                    nextState = hrCostState[0:-1]
                    minCostTileState = hrCostState

            if minCostTileState in self.PreviousStates  and  minCostTileState in self.SmallestDistanceStates:
                self.SmallestDistanceStates.remove(minCostTileState) #remove state till new(min cost) one not come

            else:
                self.PreviousStates.append(minCostTileState)
                return nextState


    def heuristicFunction(self, tileState):
        heuristicDistance = 0
        #NoOfMissPlaced = 0
        
        for tile in tileState:
            heuristicDistance += math.fabs(tileState.index(tile) - self.GoalState.index(tile))

        """for tile in range(9):
            if tileState[tile] != self.GoalState[tile]:
                NoOfMissPlaced += 1"""
                
        tileState.append(heuristicDistance) # + NoOfMissPlaced)

        return tileState



    def puzzleSolver(self, tileState=[]):
        subTileState = []
        getEmptyPlace = tileState.index('-')+1
        subTileState.extend(tileState)
        movingPlaces = self.movingBoundries(getEmptyPlace)

        self.SmallestDistanceStates = []

        if getEmptyPlace+3 <= 9:
            temp = subTileState[tileState.index('-')]
            subTileState[tileState.index('-')] = subTileState[tileState.index('-')+3]
            subTileState[tileState.index('-')+3] = temp

            self.SmallestDistanceStates.append( self.heuristicFunction(subTileState) )
            subTileState = []
            subTileState.extend(tileState)

        if getEmptyPlace-3 >= 1:
            temp = subTileState[tileState.index('-')]
            subTileState[tileState.index('-')] = subTileState[tileState.index('-')-3]
            subTileState[tileState.index('-')-3] = temp

            self.SmallestDistanceStates.append( self.heuristicFunction(subTileState) )
            subTileState = []
            subTileState.extend(tileState)

        if getEmptyPlace-1 >= movingPlaces[0]:
            temp = subTileState[tileState.index('-')]
            subTileState[tileState.index('-')] = subTileState[tileState.index('-')-1]
            subTileState[tileState.index('-')-1] = temp

            self.SmallestDistanceStates.append( self.heuristicFunction(subTileState) )
            subTileState = []
            subTileState.extend(tileState)

        if getEmptyPlace+1 <= movingPlaces[1]:
            temp = subTileState[tileState.index('-')]
            subTileState[tileState.index('-')] = subTileState[tileState.index('-')+1]
            subTileState[tileState.index('-')+1] = temp

            self.SmallestDistanceStates.append( self.heuristicFunction(subTileState) )
            subTileState = []
            subTileState.extend(tileState)
        
