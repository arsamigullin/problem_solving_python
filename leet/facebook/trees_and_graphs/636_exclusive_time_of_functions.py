from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        funcs = [0] * n
        for record in logs:
            id, command, timestamp = record.split(':')
            timestamp = int(timestamp)
            # we put onto stack all the timestamps and deltas of started functions

            if command == "start":
                stack.append([timestamp, 0])
            else:
                start, delta = stack.pop()
                # since some functions could consume some time already we must subtract this consumed time (delta) from
                # pure consumed time by the current function
                # so, the time the current function is running is
                # pure_consumed_time - delta
                # here is an example
                # 4
                # ["0:start:0","1:start:2","2:start:3","2:end:4","1:end:5","0:end:8","3:start:9","3:end:10"]
                # function with id 2 starts at 3 and ends at 4
                # so, 3 and 4 (in total two time units) time units are already consumed by the function with id 2
                # when calculating consuming time for function with id 1 we must subtract pure_consumed_time of previous function
                # from the pure_consumed_time of the current function
                pure_consumed_time = timestamp + 1 - start
                funcs[int(id)] += pure_consumed_time - delta
                if stack:
                    # pass this pure_consumed_time to be counted by the next function
                    stack[-1][1]+=pure_consumed_time
        return funcs
