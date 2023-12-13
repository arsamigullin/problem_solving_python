import collections
import  random
left = [1,2,3,4,5,6,7,8,9,10,11,12]
right = [1,2,3,4,5,6,7,8,9,10,11,12]
visited = set()
dl = collections.defaultdict(int)
dr = collections.defaultdict(int)
res = []
num = 1
while len(visited)!=144:
    l = random.choice(left)
    r = random.choice(right)
    exp = f"{l} x {r} = "
    if exp in visited:
        continue
    dl[l]+=1
    dr[r]+=1
    mul = l * r
    res.append(f"{mul} / {l} =")
    #res.append(f"{mul} / {r} =")
    visited.add(exp)

if __name__ == '__main__':
    random.shuffle(res)
    num = 1
    for e in res:
        print(f"{num}. {e}")
        num+=1
    print('done')