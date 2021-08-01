class MyCalendarTwo(object):

    def __init__(self):
        self.events = []

    def book(self, start, end):
        cnt = 0
        for s, e in self.events:
            if not(start>=e or end<=s):
                cnt +=1
                if cnt>=2:
                    return False
        self.events.append((start, end))
        return True


if __name__ == '__main__':
    m = MyCalendarTwo()
    m.book(10, 20);
    m.book(50, 60);
    m.book(10, 40);
    m.book(5, 15);
    m.book(5, 10);
    m.book(25, 55);