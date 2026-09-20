from functools import reduce

l = [1, 7, 8]
r_l = reduce(lambda l1, item: [item] + l1, l, [])
print(r_l)

s = "sneha"
r_l = reduce(lambda s_i, item: item + s_i, s, "")
print(r_l)

print(reversed(range(1, 11)))

l1 = [[1, 2, 3], [0, 8], [6, 7, 5]]
l2 = [1, 2, 3, 0, 8, 6, 7, 5]
# l1_n=reduce(

print("Flattened list: ", reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], []))
print(" ".join(map(str, [1, 2, 3, 4, 5, 6, 7, 8])))

input_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]

# result = reduce(set.intersection, map(set, input_list))
print(list(map(set, input_list)))
l_names = ["sneha", "akash", "tina"]

# print((map(lambda x:{x[0]:x},l_names)))