import typing
List = typing.List

# this runs fast
class SolutionFast:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        cols = {}
        rows = {}
        pixels = []
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j]=='B':
                    rows[i] = rows.get(i,0)+1
                    cols[j] = cols.get(j,0)+1
                    pixels.append((i,j))
        cnt = 0
        for i, j in pixels:
            if rows.get(i,0) == 1 and cols.get(j,0) == 1:
                cnt += 1
        return cnt


class SolutionFastZip:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rotate_pic, ans = list(zip(*picture)), 0
        for i in range(len(picture)):
            if picture[i].count('B') == 1:
                idx = picture[i].index('B')
                if rotate_pic[idx].count('B') == 1:
                    ans += 1
        return ans


# this uses DFS and it is running more than 1 sec
class SolutionLongRunning:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture:
            return 0
        visited = set()
        N = len(picture)
        M = len(picture[0])
        dcol = {}
        drow = {}

        def helper(i, j):
            nonlocal drow
            nonlocal dcol
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            if picture[i][j] == 'B':
                drow[i] = drow.get(i, 0) + 1
                dcol[j] = dcol.get(j, 0) + 1
            res = 0
            for xoffset, yoffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + xoffset, j + yoffset
                if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
                    res += helper(i + xoffset, j + yoffset)

            if picture[i][j] == 'W':
                return res
            elif picture[i][j] == 'B':
                if drow[i] == 1 and dcol[j] == 1:
                    return res + 1
            return res

        return helper(0, 0)

if __name__ == "__main__":
    s = SolutionFastZip()
    s.findLonelyPixel([["W","W","B"],["W","B","W"],["B","W","W"]])