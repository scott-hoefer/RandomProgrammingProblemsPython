'''
SOLVED ON HACKER RANK 

We define P to be a permutation of the first n natural numbers in the range [1, n]. Let pos[i] denote the value at position i in permutation P using 1-based indexing. 

P is considered to be an absolute permutation if |pos[i] — i| = k holds true for every i in [1, n]. 

Given n and k, print the lexicographically smallest absolute permutation P. If no absolute permutation exists, print -1. 
For example, let n = 4 giving us an array pos = [1, 2, 3, 4]. If we use 1 based indexing, create a permutation where every |Pos[i] — i| = k. 
If k = 2, we could rearrange them to [3, 4, 1, 2]: 
pos[i] i 'Difference' 
3 1 2 
4 2 2 
1 3 2 
2 4 2 

Function Description: It should return an integer that represents the smallest lexicographically smallest permutation, or -1 if there is none. absolutePermutation has the following parameter(s): 
• n: the upper bound of natural numbers to consider, inclusive 
• k: the integer difference between each element and its index 

Constraints 
• 1 < n < 105 
• 0 < k < n 

Sample Input

2 1
3 0
3 2
8 2

Sample Output

2 1
1 2 3
-1
3 4 1 2 7 8 5 6

'''
def absolutePermutation(n, k):
    if k == 0:
        # edge case where k=0, then they are just in order, i.e. n-3, k=0 would print 
        # 1 2 3
        # since pos[i] (1-indexed) - i = k so pos[1] - 1 = 0 and so on
        return [x for x in range(1, n+1)] 
    # if this isn't true then there isn't a spot for each number, since we can only use each number
    # once, and no valid permutation exists       
    if (n/k) % 2 != 0:
        return [-1]
    # if there is a valid permuation, it must be either in i+k or i-k, i.e.
    # if i is 1 and k is 1 then i+k = 1+1 = 2 and thats the first number, since k is 1 and 
    # we have done i+k once, we switch to i-k, so i is now 2 and i-k = 2-1 = 1 and thats the next number
    # always start with 1+k and do that k times, then swith to i-k for k times and so on
    absPerm = []
    add = True
    for i in range(1, n+1):
        if add:
            absPerm.append(i+k)
        else:
            absPerm.append(i-k)
        # this is how we know when to switch from i+k to i-k and vice versa 
        if i % k == 0:
            if add:
                add = False
            else:
                add = True

    return absPerm


if __name__ == '__main__':
    n = 8
    k = 2
    perm_answer = absolutePermutation(n, k)
    print('the answer to absolute permutation is {} for n={}, k={}'.format(str(perm_answer), str(n), str(k)))