class Queue():
    def __init__(self):
        self.cards = []

    def push(self, card):
        self.cards.append(card)

    def pop(self):
        self.cards.pop(0)

if __name__ == '__main__':
    queue = Queue(input())
