from collections import Counter


def min_swaps(s: str) -> int:
    """
    Time  : O(N^2)
    Space : O(N), where N = len(s)
    """
    if not is_valid_palindrome(s):
        return -1

    # CONVERT TO LIST
    s = list(s)

    # SETUP FRONT BACK POINTER
    lo, hi = 0, len(s) - 1
    swaps = 0

    # LOOP TILL CROSS
    while lo < hi:

        # CASE 1 - FRONT = BACK
        if s[lo] == s[hi]:
            lo += 1
            hi -= 1

        # CASE 2 - FRONT != BACK
        else:

            # FIND THE RIGHTMOST CHAR TO MATCH THE FRONT
            mid = hi
            while mid > lo and s[lo] != s[mid]:
                mid -= 1

            # CASE 1 - CHAR NOT FOUND - SWAP ONCE WITH RIGHT NEIGHBOR, AND CONTINUE WITHOUT CLOSING WINDOW
            # THIS LONER CHAR WILL EVENTUALLY END UP IN THE MIDDLE OF THE STRING
            if mid == lo:
                s[mid], s[mid + 1] = s[mid + 1], s[mid]
                swaps += 1
                continue

            # CASE 2 - CHAR FOUND - SWAP WITH RIGHT NEIGHBOR UNTIL IT ENDS UP AT THE BACK
            for i in range(mid, hi):
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1

            # CLOSE THE WINDOW
            lo += 1
            hi -= 1

    return swaps


def is_valid_palindrome(s: str) -> bool:
    count = Counter(s)
    return len([char for char, freq in count.items() if freq % 2]) <= 1


if __name__ == "__main__":
    print(min_swaps("asflkj") == -1)
    print(min_swaps("mamad") == 3)
    print(min_swaps("aabb") == 2)
    print(min_swaps("ntiin") == 1)



