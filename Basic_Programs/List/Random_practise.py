# Python Program to Split Even and Odd Elements into Two Lists
l = [int(input("Enter number: ")) for _ in range(5)]
even = [each for each in l if each % 2 == 0]
odd = [each for each in l if each % 2 != 0]
print(f"Even: {even} Odd: {odd}")

# Python Program to Count Occurrences of Element in List
occurence = {}

for each in l:
    occurence[each] = occurence[each] + 1 if each in occurence else 1
print(f"Count of Occurrences of Elements in List: {occurence}")

# Remove Duplicates from a List
occurence = {key : item for key, item in occurence.items() if occurence[key] != 2}

print(f"New list: {list(occurence.values())}")
