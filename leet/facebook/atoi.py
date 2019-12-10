def myAtoi(s):
    if s == "":
        return 0
    start = 0
    for c in s:
        if c == ' ':
            start += 1
        else:
            break

    stripped_str = s[start:len(s)]
    sign_coef = 1
    if len(stripped_str) > 0:
        if stripped_str[0] == '-':
            sign_coef = -1
            stripped_str = stripped_str[1:len(stripped_str)]
        elif stripped_str[0] == '+':
            sign_coef = 1
            stripped_str = stripped_str[1:len(stripped_str)]

    if len(stripped_str) > 0 and not stripped_str[0].isnumeric():
        return 0
    num = ""
    for c in stripped_str:
        if c.isnumeric():
            num += c
        else:
            break
    if num == "":
        return 0
    conv_num = int(num) * sign_coef
    if -2147483648 > conv_num:
        return -2147483648
    if conv_num > 2147483647:
        return 2147483647
    return conv_num

if __name__ == "__main__":
    myAtoi('')