def solution(s):
    d = dict()
    def find(i,j):
        if i>j:
            return 0
        if i==j:
            return 1
        if s[i] == s[j]:
            return find(i+1, j-1) + 2
        key = str(i)+"|"+str(j)
        #print(key)
        if key not in d:
            d[key] = max(find(i+1,j), find(i,j-1))
        return d[key]
    find(0, len(s) - 1)
    print(d)


if __name__ == "__main__":
    print(solution("abcdeca"))
    #print(solution("fcgihcgeadfehgiabegbiahbeadbiafgcfchbcacedbificicihibaeehbffeidiaiighceegbfdggggcfaiibefbgeegbcgeadcfdfegfghebcfceiabiagehhibiheddbcgdebdcfegaiahibcfhheggbheebfdahgcfcahafecfehgcgdabbghddeadecidicchfgicbdbecibddfcgbiadiffcifiggigdeedbiiihfgehhdegcaffaggiidiifgfigfiaiicadceefbhicfhbcachacaeiefdcchegfbifhaeafdehicfgbecahidgdagigbhiffhcccdhfdbd"))