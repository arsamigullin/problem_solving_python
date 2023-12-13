import collections
import  random
left = [1,2,3,4,5,6,7,8,9,10,11,12]
right = [1,2,3,4,5,6,7,8,9,10,11,12]
visited = set()
dl = collections.defaultdict(int)
dr = collections.defaultdict(int)

num = 1
while len(visited)!=144:
    l = random.choice(left)
    r = random.choice(right)
    exp = f"{l} x {r} = "
    if exp in visited:
        continue
    dl[l]+=1
    dr[r]+=1
    visited.add(exp)
    print(f"{num}. {exp}")
    num+=1

if __name__ == '__main__':
    print(dl)
    print(dr)
    print("done")
