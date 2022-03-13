from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        SINGLE_LINE_COMMENT = '//'
        MULTI_LINE_COMMENT_START = '/*'
        MULTI_LINE_COMMENT_END = '*/'
        is_multi_line_comment = False  # this is to check if the current symbol withing multiline comment
        CONTINUATION = '#'
        for line in source:
            code = []
            i = 0
            while i < len(line):
                #  we've got //, stop
                if line[i:i + 2] == SINGLE_LINE_COMMENT and not is_multi_line_comment:
                    break
                # the multiline comment started
                elif line[i:i + 2] == MULTI_LINE_COMMENT_START and not is_multi_line_comment:
                    is_multi_line_comment = True
                    code.append(CONTINUATION)  # append this special char, use it to join multiline comments
                    i += 1
                elif line[i:i + 2] == MULTI_LINE_COMMENT_END and is_multi_line_comment:
                    # if start and end of multiline comment are on the same line, extract special char
                    # this is to cover cases like this
                    # ["a/*comment", "line", "more_comment*/b"]
                    # a and b  should be concatenated representing single line of code
                    if code and code[-1] == CONTINUATION:
                        code.pop()
                        is_multi_line_comment = False
                        i += 1
                elif not is_multi_line_comment:  # add char if it is not in the multiline comment
                    code.append(line[i])
                i += 1

            # check if we want to join the collected code of the current line the to the code on the last line
            # this is to cover cases like this
            # ["a/*comment", "line", "more_comment*/b"]
            # a and b  should be concatenated representing single line of code
            if result and result[-1][-1] == CONTINUATION and not is_multi_line_comment:
                last_line = result.pop()[:-1] + ''.join(code)
                if last_line:
                    result.append(last_line)
            else:  # otherwise, just add new line of code
                if code:
                    result.append(''.join(code))


        return result

if __name__ == '__main__':
    s = Solution()
    s.removeComments(["a/*comment", "line", "more_comment*/b"])
    s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])