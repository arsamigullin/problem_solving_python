from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        cnt = i = j = 0
        while i < len(chars):
            if chars[i] != chars[j]:
                if cnt >= 2:
                    end = str(cnt)
                    chars[j + 1:j + 1 + len(end)] = list(end)
                    j += len(end) + 1
                else:
                    j += 1

                chars[j] = chars[i]
                cnt = 0
            i += 1
            cnt += 1
        if cnt >= 2:
            end = str(cnt)
            chars[j + 1:j + 1 + len(end)] = list(end)
            j = j + len(end) + 1
        else:
            j += 1

        return j

class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write