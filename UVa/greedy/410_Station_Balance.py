def main():
    chamber_count, specimens_count = map(int, input().split())
    specimens = list(map(int, input().split()))

    dummy_count = 2 * chamber_count - specimens_count
    for i in range(dummy_count):
        specimens.append(0)

    specimens.sort()
    i, j = 0, len(specimens) - 1
    avg = sum(specimens)//chamber_count
    imbalance = 0
    set_num = 1
    while i<j:
        print(f"Set #{set_num}")
        msg= f" {set_num-1}:"
        if specimens[i]>0:
            msg+=f" {specimens[i]}"
        if specimens[j]>0:
            msg+=f" {specimens[j]}"
        imbalance += abs(specimens[i] - specimens[j]) - avg
        print(msg)
        i+=1
        j-=1
        set_num+=1


    print(f"IMBALANCE = {imbalance}")

if __name__ == '__main__':
    main()



