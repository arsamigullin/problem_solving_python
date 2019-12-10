
#https://www.rapidtables.com/convert/number/binary-to-decimal.html
#1110012 = 1⋅2**5+1⋅2**4+1⋅2**3+0⋅2**2+0⋅2**1+1⋅2**0 = 5710
#1110012 - those are coefs
def solution(a,b):
    def conv(num):
        n = len(num) - 1
        res = 0
        for c in num:
            res += (ord(c) - 48) * 2**n
            n-=1
        return res

    dec_res = conv(a) + conv(b)
    res_bin = ""
    while dec_res > 0:
        dec_res, mod = divmod(dec_res, 2)
        res_bin+=str(mod)
    return res_bin[::-1] # do not forget to reverse

#shortest solution
def add_binary2(self, a, b):
    return '{0:b}'.format(int(a, 2) + int(b, 2))


# Approach 1: Bit-by-Bit Computation
def bit_by_bit_computation(a, b):
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    carrier = 0
    answer=[]

    for i in range(n-1, -1, -1):
        if a[i] == '1':
            carrier+=1
        if b[i] == '1':
            carrier+=1
        if carrier%2 == 1:
            answer.append('1')
        else:
            answer.append('0')
        carrier//=2 # here we calculated the next carrier

    if carrier == 1:
        answer.append(1)
    answer.reverse()
    return ''.join(answer)

# bit manipulation technique
# #Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.
#While carry is nonzero: y != 0:
#Current answer without carry is XOR of x and y: answer = x^y.
#Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
#Job is done, prepare the next loop: x = answer, y = carry.
#Return x in the binary form.
def add_binary(a, b):
    x, y = int(a, 2), int(b, 2)
    while y:
        x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]

if __name__ == "__main__":
    bit_by_bit_computation("11", "1")
    solution("0", "0")
    solution("11", "1")
