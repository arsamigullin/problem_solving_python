from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)

        q = deque([(startGene, 0)])

        while q:
            gene, muts = q.popleft()
            if gene == endGene:
                return muts
            for ch in ['A', 'C', 'G', 'T']:
                for i in range(len(gene)):
                    if ch != gene[i]:
                        neighbor_gene = gene[:i] + ch + gene[i + 1:]
                        if neighbor_gene in bank:
                            q.append((neighbor_gene, muts + 1))
                            bank.discard(neighbor_gene)
        return -1

    