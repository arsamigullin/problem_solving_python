#https://leetcode.com/problems/unique-email-addresses/

# Algo
# 1. Split by @
# 2. Split by + and take first elemet of array
# 3. Split by '.' and join the elements
class SolutionMy:
    def numUniqueEmails(self, emails: list) -> int:
        d = {}
        for email in emails:
            localname, domain = email.split('@')
            modif_email = ''.join(localname.split('+')[0].split('.')) + '@' + domain
            if modif_email not in d:
                d[modif_email] = 1
        return len(d)
