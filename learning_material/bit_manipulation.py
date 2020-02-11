
if __name__ == "__main__":
    for i in range(1, 32):
        pass
        #print(f"{i}&1 = {i & 1}")
# num&1 = 1 for odd num
# num&1 = 0 for even num

for i in range(1, 32):
    print(f"{i}>>1 = {i >> 1}")

# Check if the number is a power of 2?
x = 4
x & x - 1 == 0