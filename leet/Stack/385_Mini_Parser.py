class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        i = 0

        def helper():
            nonlocal i
            # if i>=len(s):
            #     return None
            if s[i] == '[':
                i += 1
                nest_list = NestedInteger()
                while i < len(s) and s[i] != ']':
                    nest_list.add(helper())
                    if s[i] == ',':
                        i += 1
                i += 1
                return nest_list

            else:
                start = i
                while i < len(s) and s[i] != ',' and s[i] != ']':
                    i += 1
                return NestedInteger(int(s[start:i]))

        return helper()

    # eval solution
    def deserialize(self, s):
        def nestedInteger(x):
            if isinstance(x, int):
                return NestedInteger(x)
            lst = NestedInteger()
            for y in x:
                lst.add(nestedInteger(y))
            return lst

        return nestedInteger(eval(s))