import operator


class Ranks(object):
    poker = 1
    full = 2
    flush = 3
    straight = 4
    drill = 5
    two_pair = 6
    pair = 7
    high = 8
    open_flush = 9
    open_straight = 10
    nothing = 11


class Rank(object):
    cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    really_high_card = ['A', 'K', 'Q']
    high_card = ['A', 'K', 'Q', 'J', '10']
    high_enough_card = ['A', 'K', 'Q', 'J', '10', '9', '8']

    def __init__(self, our_cards, community_cards):
        self.our_cards = our_cards
        self.community_cards = community_cards
        self.counts = {
            "A": 0, "K": 0, "Q": 0, "J": 0, "10": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0
        }
        self.suits = {
            "spades": 0,
            "hearts": 0,
            "clubs": 0,
            "diamonds": 0
        }
        self.init()

    def init(self):
        for c in self.our_cards:
            self.counts[c["rank"]] += 1
        for c in self.community_cards:
            self.counts[c["rank"]] += 1

        for c in self.our_cards:
            self.suits[c["suit"]] += 1
        for c in self.community_cards:
            self.suits[c["suit"]] += 1

        self.max0 = max(self.counts.iteritems(), key=operator.itemgetter(1))
        self.counts0 = dict(filter(lambda x: x[0] != self.max0[0], self.counts.items()))
        self.max1 = max(self.counts0.iteritems(), key=operator.itemgetter(1))
        self.counts1 = dict(filter(lambda x: x[0] != self.max1[0], self.counts0.items()))
        self.max2 = max(self.counts1.iteritems(), key=operator.itemgetter(1))
        self.counts2 = dict(filter(lambda x: x[0] != self.max2[0], self.counts1.items()))

        self.maxsuit = max(self.suits.iteritems(), key=operator.itemgetter(1))[1]

    def maxSeriesLength(self):
        mx = 0
        m = 0

        for c in self.cards:
            if self.counts[c] == 1:
                m += 1
            else:
                if m > mx:
                    mx = m
                m = 0
        if m > mx:
            mx = m

        if mx < 5 and m > 0:
            if self.counts["A"] == 1:
                mx += 1

        return mx

    def maxSameSuit(self):
        return self.maxsuit

    def isStraight(self):
        ml = self.maxSeriesLength()
        return ml == 5

    def getRank(self):
        if self.max0[1] == 4:
            return Ranks.poker
        elif self.max0[1] == 3 and self.max1[1] == 2:
            return Ranks.full
        elif self.maxsuit == 5:
            return Ranks.flush
        elif self.isStraight():
            return Ranks.straight
        elif self.max0[1] == 3:
            return Ranks.drill
        elif self.max0[1] == 2 and self.max1[1] == 2:
            return Ranks.two_pair
        elif self.max0[1] == 2:
            return Ranks.pair
        else:
            return Ranks.high

    def getPossible(self):
        if self.maxSameSuit() == 4:
            return Ranks.open_flush
        elif self.maxSeriesLength == 4:
            return Ranks.open_straight
        else:
            return "none"

    def dump(self):

        print self.max0
        print self.max1
        print self.max2
        print "MS " + str(self.maxsuit)
        print self.getRank()
        print self.getPossible()

    def dangerStraight(self):
        if self.maxSeriesLength() >= 4:
            return True

    def danger(self):
        r = Rank({}, self.community_cards)
        if r.maxSameSuit() >= 4:
            return True
        if r.dangerStraight():
            return True
        if r.getRank() in [Ranks.pair, Ranks.two_pair] and r.getRank() in [Ranks.pair]:
            return True
        return False


if __name__ == '__main__':
    our_cards = {
                    "rank": "A",
                    "suit": "hearts"
                }, {
                    "rank": "5",
                    "suit": "diamonds"
                }
    community_cards = {
                          "rank": "4",
                          "suit": "hearts"
                      }, {
                          "rank": "4",
                          "suit": "hearts"
                      }, {
                          "rank": "2",
                          "suit": "hearts"
                      }

    cards = Rank(our_cards, community_cards)
    print cards.getRank()
    cards.dump()
