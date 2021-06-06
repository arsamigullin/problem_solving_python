import collections
# Red, Green, Blue, Yellow, Violet, Gray, Orange
col_dict = {1:'red', 2: 'green', 3: 'blue', 4:'yellow', 5:'violet', 6:'gray',7:'orange'}
def solution(edges, n):

    graph = collections.defaultdict(list)
    colors = collections.defaultdict(int)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        colors[u] = 0
        colors[v] = 0

    visited = set()
    def dfs(i):
        visited.add(i)
        tot_colors = {1,2,3,4,5,6,7}
        children_colors = {colors[ch] for ch in graph[i]}
        av_colors = tot_colors.difference(children_colors)
        if len(av_colors) == 0:
            #print(f"Not Possible with 7 colors.")
            return False
        colors[i] = av_colors.pop()
        print(f"{i} Colored to {col_dict[colors[i]]}")
        is_possible = False
        colored_neighbors = 0
        for child in graph[i]:
            if colors[child] == 0:
                if dfs(child):
                    is_possible = True
                    break
            else:
                colored_neighbors+=1
        return is_possible or colored_neighbors == len(graph[i])


    for i in range(0,n):
        if i not in visited:
            if not dfs(i):
                print('not possible')



if __name__ == '__main__':
    solution([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)], 6)
    print('done')
    #solution([[1,2],[2,3],[1,3],[1,4],[4,3],[5,5]],5)
    solution([[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[1,2],[2,3],
              [3,4],[4,5],[5,6],[1,3],[1,4],[2,4],[2,5],
              [2,6],[3,6],[4,6],[1,5],[3,5],[1,6],[7,8],
              [1,8],[2,8],[3,8],[4,8],[5,8],[6,8]],8)

