# https://github.com/worldveil/deuces
# actual lib is https://github.com/ihendley/treys

from treys import Card, Evaluator
from copy import deepcopy

class CardCentroid:

    def __init__(self) -> None:
        self.allCards = self.generate_card_array()
        self.allCardPairs = self.generate_card_pairs(self.allCards)
        self.evaluator = Evaluator()

    def getEquityAllCards(self, holeCards, tableCards):
        
        all_cards = deepcopy(holeCards)
        all_cards.extend(tableCards)

        possible_opp_pairs = [(card1, card2) for (card1, card2) in self.allCardPairs if card1 not in all_cards and card2 not in all_cards]
        opp_pair_cards = [(Card.new(x), Card.new(y)) for (x,y) in possible_opp_pairs]
        
        holeCard_object = (Card.new(holeCards[0]), Card.new(holeCards[1]))
        tableCard_object = (Card.new(tableCards[0]), Card.new(tableCards[1]), Card.new(tableCards[2]), Card.new(tableCards[3]), Card.new(tableCards[4]))
        player_score = self.evaluator.evaluate(holeCard_object, tableCard_object)

        opp_pair_scores = []
        for pair in opp_pair_cards:
            opp_pair_scores.append(self.evaluator.evaluate(pair, tableCard_object))

        equal_count = 0
        less_count = 0
        all_count = len(opp_pair_scores)
        
        for num in opp_pair_scores:
            if num == player_score:
                equal_count += 1
            elif num > player_score:
                less_count += 1

        return (less_count / all_count) + 0.5 * (equal_count / all_count)

    # Given a map of every possible card pair scores, given cards to exclude, return remaining pair/scores
    # 

    def generate_card_pairs(self, cards):
        pairs = []
        n = len(cards)
        for i in range(n):
            for j in range(n):
                pair = (cards[i], cards[j])
                reverse_pair = (cards[j], cards[i])
                if pair not in pairs and reverse_pair not in pairs and (i != j):
                    pairs.append(pair)
        
        return pairs

    def generate_card_array(self):
        ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        suits = ['h', 'd', 's', 'c']
        cards = []
        for rank in ranks:
            for suit in suits:
                cards.append(rank + suit)

        return cards
