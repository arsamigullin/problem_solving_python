arr = iter((list([2,4,5])))

def main():
    n = next(arr)

    while n > 0:
        n -= 1
        cards = next(arr)
        deck = []

        for i in range(cards, 0, -1):
            deck.insert(0, i)

            for j in range(0, i):
                deck.insert(0, deck.pop())

        print(' '.join(deck))

        print("")

if __name__ == "__main__":
    main()