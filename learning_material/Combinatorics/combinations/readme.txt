The interpretation of this problem depends on the interviewer. There are three possible scenarios:
You could be asked to implement \mathcal{O}(1)O(1) runtime by precomputing all the combinations.
Or, you could be asked to save space, to use no precomputation and to implement the nextCombination function
to generate each new combination from the previous one during the runtime.
Or, the interviewer could let you choose one of the problems above and then asks you to implement the second one as a follow-up.

Using backtracking approach will not be the best option because it will not allow you getting the next combination
if you just need to get only it.
On the other hand Bitmask approach and algorithm L by Knuth has an ability to generate the next combination. So, you
wrote an algo to generate all combinations you also can easily swithch to the gettin the next combination