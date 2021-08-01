import collections


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        q = collections.deque()
        n = len(dominoes)
        dist = [-1] * n
        for i, d in enumerate(dominoes):
            if d in {'L', 'R'}:
                q.append(i)
                dist[i] = 0

        while q:
            i = q.popleft()
            node = dominoes[i]
            if node == 'R' and i + 1 < n:
                nei = i+1
                if dominoes[nei] == '.' and dist[nei] == -1:
                    dominoes[nei] = 'R'
                    dist[nei] = dist[i] + 1
                    q.append(nei)
                elif dominoes[nei] == 'L' and dist[i] < dist[nei]:
                    dominoes[nei] = '.'
            elif node == 'L' and i - 1 >= 0:
                nei = i-1
                if dominoes[nei] == '.' and dist[nei] == -1:
                    dist[nei] = dist[i] + 1
                    dominoes[nei] = 'L'
                    q.append(nei)
                elif dominoes[nei] == 'R' and dist[i] < dist[nei]:
                    dominoes[nei] = '.'
        return ''.join(dominoes)


if __name__ == '__main__':
    s = Solution()
    s.pushDominoes(".L.R...LR..L..")