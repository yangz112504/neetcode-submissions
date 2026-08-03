from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find helpers
        n = len(accounts)
        parent = [i for i in range(n)]
        
        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            parent[rootA] = rootB
            return True
        
        # basically we map each email to the first account index where it appears
        # if it appears again, we union it, or basically join the two emails into both appearing from the same account rather than diferent one
        emailToAccounts = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email not in emailToAccounts:
                    emailToAccounts[email] = i
                else: # conflict
                    union(i, emailToAccounts[email])
        
        # mapping each email to the root, because that is their original account creator
        rootToEmail = defaultdict(list)
        for email, accountIndex in emailToAccounts.items():
            rootIndex = find(accountIndex)
            rootToEmail[rootIndex].append(email)
        
        # formatting the output
        res = []
        for rootIndex, emails in rootToEmail.items():
            name = accounts[rootIndex][0]
            res.append([name] + sorted(emails))
        return res
        
        








        