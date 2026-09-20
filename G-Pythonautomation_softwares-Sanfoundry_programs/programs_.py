# dtt = {"A":1,"B":100,"C":{"D":{"E":20}}}
# # print(dtt["C"]["D"]["E"])
#
# def func_d(d,key):
#
#     for k in d:
#         if key == k:
#             return d[k]
#         elif isinstance(d[k],dict):
#
#             return func_d(d[k],key)
#
# print(func_d(dtt,"E"))

from collections import defaultdict
def groups_per_user(group_dictionary):
    user_groups = defaultdict(list)
    for grp,users in group_dictionary.items():
        for user in users:
            user_groups[user].append(grp)
    return(dict(user_groups))

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))