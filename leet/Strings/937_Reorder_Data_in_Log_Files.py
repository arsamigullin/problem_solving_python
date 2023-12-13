from typing import List


# option 1
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_logs = []
        let_logs = []
        for log in logs:
            id = self.extract_id(log)
            is_dig_log = log[len(id) + 1].isdigit()
            if is_dig_log:
                dig_logs.append(log)
            else:
                log_content = log[len(id):]
                let_logs.append((log_content, id))
        let_logs.sort()
        return list(map(lambda item: item[1] + item[0], let_logs)) + dig_logs

    def extract_id(self, item):
        for i in range(len(item)):
            if item[i] == ' ':
                break
        return item[:i]

# option 2
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def cmp(log):
            _id, content = log.split(" ", maxsplit=1)
            return (0, content, _id) if content[0].isalpha() else (1,)

        logs.sort(key=cmp)
        return logs