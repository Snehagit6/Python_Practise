# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    # Create a set to store positive integers from the array
    positive_integers = set() # Set employs hashtable data structure , which allows for O(1) average time complexity for lookups and insertions.List will have O(n) time complexity for lookups, as it requires scanning through the list to find an element.

    # Iterate through the array and add positive integers to the set
    for num in A:
        if num > 0:
            positive_integers.add(num)

    # Start checking from 1 for the smallest missing positive integer
    smallest_missing = 1

    # Increment smallest_missing until we find a number not in the set
    while smallest_missing in positive_integers: # o{N} time complexity for this while loop in worst case scenario, as we may have to check all positive integers up to the maximum value in the array.
        smallest_missing += 1

    return smallest_missing