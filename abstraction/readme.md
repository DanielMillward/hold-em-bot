pre_centroids, flop_centroids, turn_centroids, river_centroids = makeCardCentroids()
big_map = makeBigMap()
saveToFile(big_map)

extern def hashInfoState()



Steps:
1. Creates card clusters
 - Preflop is 169 combos, every other turn is 770. Paper shows that a 169/9000/9000/9000 combo worked best vs a same total size 10/100/1000/10000 combo, so going with all other ones are the same size.
2. Run through infostate and every possible child
 - 

3,140,844,486 card combinations

For example, if the public board cards are 7dQh4h2s3c, then
KcQc has an equity of 0.856 against a uniform random op-
ponent hand; so the histogram entry corresponding to the
column for an equity of 0.84–0.86 is incremented by one for
this hand (prior work has assumed that the equities are di-
vided into 50 regions of size 0.02, as do these figures)

Preflop - no card abstraction
flop/turn - make histograms with given info (e.g. have it set in stone the first 3 cards are a,b, and c, only do probability for remaining 2/1) with k means with EMD
river - k means with L2 over vectors of EHS against first-round clusters of the opponent
Explained:
Assuming unsuited opponent cards, there are only 169 combinations. These are grouped into 8 buckets (see page 5 of original_card_abstraction). Get the EHS of the hole cards+public cards against each of these buckets, then do L2 distance to find the clusters

For preflop, only "buckets" are all combos, ignoring suit unless they're the same suit. See chart on page 5. If they're different suits, start from left and find the other going right. If they're the same suit, start from top, find the other going down. - **169** buckets.

For flop - a buckets

For turn - b buckets

For river - c buckets

169 + a + b + c = 2500
