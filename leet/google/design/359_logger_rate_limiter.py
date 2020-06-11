import collections


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # if this is first incoming message
        # it should always be printed
        if self.d.get(message, None) is None:
            self.d[message] = timestamp
            return True


        shouldPrint = timestamp - self.d[message] >= 10
        # we store new time only if the message has not been printed more than 10 secs
        if shouldPrint:
            self.d[message] = timestamp
        return shouldPrint
