2 - p1 stack
2 - p2 stack
2 - p1 bet amount
2 - p2 bet amount
2 - hole cards
4 - table cards
1 - Can Check: 2
1 - P1 or P2: 2
1 - Round: 4
1 - All above: 16

18 bytes

Goal sizes:
Can Check: 2
P1 or P2: 2
Round: 4
Stack/bet sizes: 1500
card abstraction sizes: 2500
- 169 / 770 / 770 / 770
- Adding, since after each round a bunch of branches merge since you don't remember what happened in the previous hand



3,140,844,486 x 5980 * 5980 * 2 * 2 * 6000 * 4 = 
10,782,514,000,000,000,000,000

goal: cut down to 50/60 million
60,000,000

### Stack and bet sizes

https://www.quora.com/What-is-the-number-of-solutions-of-a+b+c-15-with-non-negative-integer-values-for-a-b-and-c 
1bet + 1stack + 2bet + 2 stack = 3000
(n + r - 1) choose (r - 1), n = 3000, r = 4
3003 choose 3 = 4,509,005,501
Goal = 1500, so need n = 19
(19+3) choose 3 = 1540

20 40 80 160 320 640 1280 -> 20 * 2^ax
20*(2*\*(0.380*i))

20
26
34
44
57
75
97
126
164
214
279
363
472
614
799
1040
1353
1761
2291
2980

Sigmoid
3000/(1+2.178*\*(6.5-0.8*i))
20
24
33
43
68
265
459
755
1156
1617
2056
2407
2650
2801
2890
2940 50
2968 28
2982 14
2991 9
2995 4


23
36
58
93
147
231
357
538
785
1095
1449
1811
2143
2417
2625
2772
2872
2937
2979
3006

### Card distributions

Player hole cards: 1326
Table: 2118760 (5) + 230300 (4) + 19600  (3) + 1 (0) = 2368661
All above:  3,140,844,486 combinations

Find EHS of each hand+table combination? noting that sometimes less than 5 are present

calculateHandStrength(holeCards, tableCards)
Final round histograms would just be a single line at the hand strength bucket.



## Others

Can Check: 2
P1 or P2: 2
Round: 4
All above: 16


1. Start with smallest possible abstraction you can

Middleman: Makes Abstraction, Loads GB file into memory, takes infostates and gets actions, or infostates/new actions and updates them
- init()
- generateAbstractionFile(abstractionSizesAndFunctionsFilePath, infostateObjForm, MAX_ACTIONS) -> saves actual data, so when adding an action it doesn't check closest of the changed infostate, finds closest of underlying game stats
- loadAbstractionToMemory(filePath)
- saveAbstractionToDisk(filePath)
- hashInfostate(infostateObj)
- getActionProbs(infostateHash)
- updateActionProbs(infostateHash, newActionProbsObject)
- getDeterminateActionsFromInfoState(infostate) -> so can known what actions [0:7] are mapped to

CardAbstractor: Takes in number of abstractions requested, performs mini batch k-means clustering, then returns the centroids. Also provides a function that takes a hand, finds its score, and returns the index of the nearerst centroid (so don't have to store future ones.)
- doMiniBatchClustering(numBuckets, optionCards=testSubset) -> testSubset={10h, 10c, 10d, 10s, Jh, ...}
- getBucketIndex(cardHandArray)

TESTING:
- test HS of final round based on values found in the paper
- compare histograms of paper
- use the metrics of cluster goodness discussed in 472 to verify the buckets make sense.

Trainer: Runs cfr, has Middleman attribute it uses as a Model
- LoadModelRunCFRAndSaveToDisk(entryFilePath, exitFilePath)

Gamer: Allows user to use actions stored/accessed by middleman in a real game.
- runGame(modelFilePath) -> opens CLI thingy where user can type in game stats, loads and looksup infostates
- _getNewInfoState(parameterToChange, valueToAddOrChangeTo) -> can parse starting new game
- _getProbsOfInfoState(infoState)
- parseUserAction(userText) -> returns parameter, value. Param could be start new game?

Infostate (POJO)



Abstractor class
- Takes in the desired number of abstractions of the game, and a function for the bet sizes?
- outputs an object that's a middleman to a multi GB file
- middleman has a load function to get it from storage? takes a file path so that you can move it around and stuff
- also has a retrive strat by infoset thing, and a update strat for an infoset thing

- middleman loads onto the GPU? all it does is provide an interface between infostates and their actions, both read and writes.

Trainer class
- Runs cfr. 
- Can generate 8 legal actions, then finds the nearest infostates to those, makes those the child states

Gamer class
- Takes in actions, maps game state to infostate, returns strategy.
- Eventually run a tree search on subset in real time






