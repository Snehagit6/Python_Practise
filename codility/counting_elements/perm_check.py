# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element from 1 to N once, and only once.

# For example, array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function:

# def solution(A)

# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.

# Given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].


def solution(A):
    if set(A)==set(range(1,len(A)+1)):
        return 1
    return 0



print(solution([4, 1, 3, 2]))  # Output: 1
print(solution([4, 1, 3]))     # Output: 0
print(solution([1, 2, 3, 4, 5]))  # Output: 1
print(solution([-1, 2, 4, -5])) # Output: 0
print(solution([1,1,2])) # Output: 0

# Takeaway:
# Read the definition: A permutation is a sequence containing each element from 1 to Nonce, and only once.
# So in an array of length N, the elements must be exactly the numbers from 1 to N[Size of Array] with no duplicates and no missing numbers. 
# For this u need a set comparison: comparing the set of the array with the set of numbers from 1 to N. If they match, it returns 1 (indicating it's a permutation), otherwise it returns 0.


