import collections
from functools import reduce


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    res = []
    for s in strs:
        srt = reduce(lambda x, y: x + y, sorted(s))
        if srt in d:
            res[d[srt]].append(s)
        else:
            res.append([s])
            d[srt] = len(res) - 1
    return res

# elegant solution
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = collections.defaultdict(list)
    for s in strs:
        d["".join(sorted(s))].append(s)
    return d.values()


if __name__ == "__main__":
    groupAnagrams([""])
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])