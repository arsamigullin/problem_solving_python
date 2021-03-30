# https://www.mathsisfun.com/combinatorics/combinations-permutations.html
#-----------------Permutations--------------------
# Definition from Tucker
# A permutation of n distinct objects is an arrangement, or ordering, of the n objects.
# Definition from Cormen
# A permutation of a ﬁnite set S is an ordered sequence of all the elements of S,
# with each element appearing exactly once
# if S = {a,b,c}, then the permutations are
# abc; acb; bac; bca; cab; cba
# if we want to permute only 2 objects of the set
# P(n, 2) = n(n − 1),
# if we want to permute only 3 objects of the set
# P(n, 3) = n(n − 1)(n − 2),
# if we want to permute only n objects of the set
# P(n, n) = n(n − 1)(n − 2) × · · · × 3 × 2 × 1 (n!)

# the closed formula for permutation r objects in n
# P(n,r) = n!/(n-r)!


# -------------Combinations --------------------
# A k-combination of an n-set S is simply a k-subset of S. For example, the 4-set
# {a; b; c; d} has six 2-combinations:
# ab; ac; ad; bc; bd; cd
# C(n,r) = n!/(r!(n-r)!)