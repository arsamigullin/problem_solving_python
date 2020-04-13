arr = ['1','-','5','+','35','*','4']

if __name__ == "__main__":
    tot = int(arr[-1])
    for i in range(len(arr)-2, -1, -2):
        num, op = arr[i-1:i+1]
        if op == "*":
            tot*=int(num)
        elif op == "-":
            tot-=int(num)
        else:
            tot+=int(num)


