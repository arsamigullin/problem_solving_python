def solution(A):

    def find(i, cur):
        if i>=len(A):
            return 0
        total = 0
        tot = 0
        while i < len(A):
            if len(cur) >= len(A[i]):
                tot = max(tot, find(i + 1, A[i]))
                i = i + 1
            else:
                if any(A[i].count(ch) == 0 for ch in cur):
                    tot = max(tot, find(i + 1, A[i]))
                    i = i + 1
                else:
                    cur = A[i]
                    i += 1
                    total+=1
        return  max(total, tot)

    return find(1, A[0]) + 1


def solution2(A):
    A = sorted(A, key=lambda x: len(x))
    dp = [1]*len(A)
    rec = {}

    for i, word in enumerate(A):
        for j in range(len(word)):
            subword = word[:j] + word[j+1:]
            if subword in rec:
                dp[i] = max(dp[i], dp[rec[subword]] + 1)
        rec[word] = i

    return max(dp)





    return max(dp)

if __name__ == "__main__":
    print(solution2(["a","b","ba","bca","bda","bdca"]))
    s = ["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju","cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc","nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl","ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr","sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx","gxi","gqxi","heheex"]
    print(solution(sorted(s, key=lambda x: len(x), reverse=True)))