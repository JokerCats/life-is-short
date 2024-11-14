import random
from enum import Enum


# 定义花色
class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)


# for x in Suite:
#     print(f"{x} : {x.value}")


# 定义卡牌
class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self) -> str:
        suites = "♠♥♣♦"
        faces = ["", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return f"{suites[self.suite.value]}{faces[self.face]}"

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value


# print(Card(Suite.SPADE, 13))


# 定义扑克
class Poker:
    def __init__(self) -> None:
        # 创建 52 张扑克牌
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        # 发牌位置
        self.current = 0

    def shuffle(self):
        # 重置发牌索引
        self.current = 0
        # 打乱扑克牌列表
        random.shuffle(self.cards)

    def deal(self) -> Card:
        card = self.cards[self.current]
        self.current += 1
        return card


# poker = Poker()
# poker.shuffle()
# print(poker.cards)


# 定义玩家
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


poker = Poker()
poker.shuffle()
players = [Player("User001"), Player("User002"), Player("User003"), Player("User004")]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(player.name)
    print(player.cards)
