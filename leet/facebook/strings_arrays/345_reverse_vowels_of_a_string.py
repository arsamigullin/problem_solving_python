class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        i, j = 0, len(s) - 1
        string = list(s)
        while i <= j:
            left = string[i].lower()
            right = string[j].lower()
            if left in vowels and right in vowels:
                string[i], string[j] = string[j], string[i]
            elif left in vowels:
                j -= 1
                continue
            elif right in vowels:
                i += 1
                continue
            i += 1
            j -= 1

        return ''.join(string)