from pprint import pprint

queryset = [{"subject__name": "Physics", "klass__name": "7th", "medium__name": "English", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "ICSE", "links": 3}, {"subject__name": "Physics", "klass__name": "7th", "medium__name": "English", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "CBSE", "links": 3}, {"subject__name": "", "klass__name": "6th", "medium__name": "English", "category__name": "Ncert", "subject__sub_subject": "Civics", "board__name": "ICSE", "links": 1}, {"subject__name": "Biolog", "klass__name": "12th", "medium__name": "English", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "ICSE", "links": 1}, {"subject__name": "Mathematics", "klass__name": "8th", "medium__name": "Hindi", "category__name": "Solution", "subject__sub_subject": "null", "board__name": "ICSE", "links": 1}, {
    "subject__name": "Mathematics", "klass__name": "6th", "medium__name": "Hindi", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "ICSE", "links": 2}, {"subject__name": "Physics", "klass__name": "7th", "medium__name": "Hindi", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "ICSE", "links": 1}, {"subject__name": "Physics", "klass__name": "7th", "medium__name": "Hindi", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "CBSE", "links": 1}, {"subject__name": "Chemistr", "klass__name": "12th", "medium__name": "Hindi", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "ICSE", "links": 1}, {"subject__name": "Mathematics", "klass__name": "12th", "medium__name": "ngali", "category__name": "Ncert", "subject__sub_subject": "null", "board__name": "ICSE", "links": 1}]
# print(queryset[2])

l1 = 'subject__name'
l2 = 'klass__name'
l3 = 'medium__name'
l4 = 'category__name'
l5 = 'board__name'
l6 = 'subject__sub_subject'
l7 = 'links'


def check(key, tree):
    if key not in tree:
        tree[key] = {}
    return tree


def make_tree():
    # sample inputs can be always be called in real-world as it is stored in db
    tree = {}
    for data in queryset:
        # print(data.values())
        cnt = 0
        stack = []

        # for k , v in data.items():
        #     cnt += 1
        #     if k not in tree:
        #         tree[v] = {}
        #         left =
        #     if cnt == 7:
        #         break
        data = data.items()
        arr = []
        for k, v in data:
            cnt += 1
            if v == '':
                arr.append('null')
            else:
                arr.append(str(v))
            if cnt == 7:
                keyy = k
                break

        prev = []
        # print(ar)
        curtree = tree
        for j in range(7):
            # if j == 0:
            #     if arr[j] not in tree:
            #         tree[arr[j]] = {}
            # elif j == 1:
            #     if arr[j] not in tree[arr[0]]:
            #         tree[arr[0]][arr[1]] = {}
            # elif j == 2:
            #     if arr[j] not in tree[arr[0]][arr[1]]:
            #         tree[arr[0]][arr[1]][arr[2]] = {}
            # elif j == 3:
            #     if arr[j] not in tree[arr[0]][arr[1]][arr[2]]:
            #         tree[arr[0]][arr[1]][arr[2]][arr[3]] = {}
            # elif j == 4:
            #     if arr[j] not in tree[arr[0]][arr[1]][arr[2]][arr[3]]:
            #         tree[arr[0]][arr[1]][arr[2]][arr[3]][arr[4]] = {}
            # elif j == 5:
            #     if arr[j] not in tree[arr[0]][arr[1]][arr[2]][arr[3]][arr[4]]:
            #         tree[arr[0]][arr[1]][arr[2]][arr[3]][arr[4]][arr[5]] = {}
            # elif j == 6:
            #     if arr[j] not in tree[arr[0]][arr[1]][arr[2]][arr[3]][arr[4]][arr[5]]:
            #         tree[arr[0]][arr[1]][arr[2]][arr[3]
            #                                      ][arr[4]][arr[5]][k] = [arr[6]]
            if j < 5:
                if arr[j] not in curtree:
                    curtree[arr[j]] = {}
                curtree = curtree[arr[j]]

        # print()
        # print()
        # dict [key][key2][key3]

    pprint(tree)


# print(5 ** 5)


# make_tree()
# result = {}
# # [ 'classq' , 'mesium']


# for data in queryset:
#     currentTree = result
#     for _, val in data.items():
#         if val not in currentTree:
#             currentTree[val] = {}
#         currentTree = currentTree[val]
#     currentTree["leaf"] = True
#     currentTree["data"] = []

# import json
# r = json.dumps(result)
# print(r)

from pprint import pprint

queryset = [
    # {"count": 10, "subject": "math", "category": "ncert", "medium": "english"},
    {"count": 17, "subject": "math",
        "medium": "bengali", "class": "6th", "board": "cbse"},
    {"count": 17, "subject": "math",
        "medium": "bengali", "class": "7th", "board": "cbse"},
    # {"count": 8, "subject": "english", "category": "ncert", "medium": "english"},
]

result = {}
levels = ["subject", "medium", "class", "board"]
dic = defaultdict
for data in queryset:
    for i in range(len(levels)):
        key = data[levels[i]]
        if i == len(levels) - 1:

            # for data in queryset:
            #     if not ok:
            #         currentTree = result
            #         # ok = True
            #     else:
            #         # print("inheritance", currentTree["data"])
            #         currentTree = currentTree["data"][0]
            #     # pprint(currentTree)
            #     for level in levels:
            #         key = data[level]
            #         # print(data[level])
            #         # key2 = "data"
            #         if "data" not in currentTree:
            #             currentTree["data"] = [{}]
            #         if key not in currentTree["data"][0]:
            #             currentTree["data"][0][key] = {}
            #         # print(currentTree,"level")
            #         # print(currentTree[key], key)
            #         currentTree["data"] = [{}]
            #         # currentTree = currentTree[key]
            #         # print(currentTree["data"][0], currentTree[key])
            #         currentTree = currentTree["data"][0]
            #         currentTree["key"] = key
            #         currentTree["icon"] = "link"
            #         # currentTree = currentTree["data"][0]
            #     # currentTree["data"] = [{}]

            #     # pprint(currentTree)
            #     # print(currentTree["data"])

            # check all levels and see if this key is available or not

ALL = []


def check_level(tree, src):

    if "key" not in tree:
        # print(tree)
        return False

    if "data" not in tree and ("key" in tree and tree["key"] != src):
        return False

    if src in tree["key"]:
        # print(tree, ALL)
        ALL.append(True)
        # print(tree, ALL)

        return True

    for treee in tree["data"]:
        check_level(treee, src)


# print(ALL)
# start from upper and go deeper and if any condition fils branch out then and there

tree = []
levels = ["subject", "board", "medium", "class"]
all_keys = set()

# for data in queryset:


# cnt = 0
# for data in queryset:
#     currentTree = result
#     new = {}
#     prev = False
#     cnt += 1
#     for level in levels:
#         key = data[level]

#         all_keys.add(key)

#         currentTree["key"] = key
#         currentTree["icon"] = "link"

#         if "data" not in currentTree:
#             currentTree["data"] = [{}]
#         else:
#             currentTree["data"].append({})

#         prev = currentTree
#         currentTree = currentTree["data"][-1]

#     prev['leaf'] = True
#     prev.pop("data")
#     # print(result)
#     # for kk in all_keys:
#     #     print(check_level(result, kk), kk, result)
#     #     if kk == "6th":
#     #         break
#     #     print()
#     #     # break
#     kk = "6th"
#     check_level(result, kk)
#     print(ALL)
#     if cnt == 1:
#         break

# pprint(tree)


import json
r = json.dumps(result)
# pprint(result)
# print(r)
# myfunc()

# all_subject = []
# all_class = []
# all_medium = []
# all_category = []
# all_sub_subject = []

# non_valid = ['{', '}', '[', ']']
# while True:
#     try:
#         for j in range(6):
#             s = input()
#             ok = True
#             for k in non_valid:
#                 if k in s:
#                     ok = False
#                     break
#             if not ok:
#                 break
#             s = s.split(':')
#             if len(s) == 1:
#                 break
#             left = s[0].strip(' ').strip('"')
#             right = s[1].strip(',')
#             if j == 0:
#                 all_subject.append(right)
#             elif j == 1:
#                 all_class.append(right)
#             elif j == 2:
#                 all_medium.append(right)
#             elif j == 3:
#                 all_category.append(right)
#             elif j == 4:
#                 all_sub_subject.append(right)
#     except:

#         break
# # print(all_subject)
# # print(all_class)
# # print(all_medium)
# # print(all_category)
# # print(all_sub_subject)
