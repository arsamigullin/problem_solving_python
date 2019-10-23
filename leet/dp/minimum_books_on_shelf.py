def solution(books, shelf_width):
    n = len(books)
    d = dict()

    def find_min_height(i):
        if i >= n:
            return 0
        min_height = float('inf')
        width = 0
        height = 0

        while i < n and width + books[i][0] <= shelf_width:
            width += books[i][0]
            height = max(height, books[i][1])
            key = str(i) + "|" + str(width)
            if key in d:
                print(key)
                min_height = min(min_height, d[key])
            else:
                min_height = min(min_height, find_min_height(i + 1) + height)
                d[key] = min_height
            i += 1
        return min_height

    return find_min_height(0)


if __name__ == "__main__":
    print(solution([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
