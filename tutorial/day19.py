from enum import Enum
import random


# 定义花色
class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)


# for suite in Suite:
#     print(f"{suite}:{suite.value}")


# 定义卡牌
class Card:
    def __init__(self, suite, face):
        # 获取花色
        self.suite = suite
        # 获取点数
        self.face = face

    def __repr__(self):
        suites = "♠♥♣♦"
        faces = ["", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return f"{suites[self.suite.value]}{faces[self.face]}"

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value


# card = Card(Suite.CLUB, 1)
# print(card)


# 定义扑克
class Poker:
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card


# poker = Poker()
# poker.shuffle()
# print(poker.cards)


# 定义家玩
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    # 摸牌
    def get_one(self, card):
        self.cards.append(card)

    # 排序
    def arrange(self):
        self.cards.sort()


# 拿出一副扑克牌
poker = Poker()
# 洗牌
poker.shuffle()
# 确认参与游戏人员
players = (Player("User1"), Player("User2"), Player("User3"), Player("User4"))
# 发牌
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
# 展示玩家手中扑克牌
for player in players:
    # 将玩家手中的牌进行排序
    player.arrange()
    print(f"{player.name}: ", end="")
    print(player.cards)
