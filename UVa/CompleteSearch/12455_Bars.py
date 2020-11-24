#tests = iter(['4','25','4','10 12 5 7','925','10','45 15 120 500 235 58 6 12 175 70','120','5','25 25 25 25 25','0','2','13 567'])
#tests = iter(['1','0','2','13 567'])
tests = iter(['20','793','19','29 21 25 36 2 22 1 39 26 8 18 30 2 35 52 23 19 47 15','427','16','2 61 59 10 46 13 52 17 2 34 12 2 60 13 41 3','660','4','63 230 167 200','431','1','431','389','13','4 71 25 30 3 40 7 29 35 27 20 71 27','419','17','9 41 38 46 2 46 11 39 13 38 47 7 16 8 32 23 3','724','16','38 38 53 33 12 24 34 22 63 41 46 40 13 5 61 57','535','10','84 67 96 20 40 45 14 82 6 81','489','11','91 70 4 56 15 16 1 82 85 68 1','579','14','19 64 6 52 64 46 29 30 66 11 35 64 66 27','911','11','8 64 86 38 47 8 58 83 87 74 57','502','9','81 5 4 106 8 100 34 92 72','325','1','237','355','16','21 45 31 7 18 5 39 55 12 15 4 13 7 10 56 17','639','14','40 69 70 49 63 59 9 19 15 69 24 62 28 63','316','9','1 22 50 51 58 95 24 2 13','479','6','30 155 9 72 164 49','870','1','870','388','14','38 40 25 55 56 6 13 6 12 60 1 3 27 46','544','5','113 35 126 157 113'])
def main():
    N = int(input())
    #N = int(next(tests))
    for _ in range(N):
        target = int(input())
        p = int(input())
        bars = map(int, input().split())
        # target = int(next(tests))
        # p = int(next(tests))
        # bars = map(int, next(tests).split())
        if target == 0:
            print('YES')
            continue
        subs = [[]]
        possible = False
        for num in bars:
            new_subs = []
            for subset in subs:
                res = subset + [num]
                if sum(res) == target:
                    possible = True
                    break
                new_subs.append(res)
            if possible:
                break
            subs+=new_subs

        print('YES' if possible else 'NO')


def all_combinations_with_bits(n,target):
    l = list(range(n))
    for i in range(1<<n):
        _sum = 0
        for j in (n):
            if i&(1<<j):
                _sum += l[j]
            if _sum == target:
                break





if __name__ == '__main__':
    main()