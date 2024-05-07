from collections import defaultdict
import json

queryset = [
    {
        "subject__name": "Physics",
        "klass__name": "7th",
        "medium__name": "Englishmed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 3,
    },
    {
        "subject__name": "Physics",
        "klass__name": "7th",
        "medium__name": "Englishmed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "CBSE",
        "links": 3,
    },
    {
        "subject__name": "SST",
        "klass__name": "6th",
        "medium__name": "Englishmed",
        "category__name": "Ncert",
        "subject__sub_subject": "Civics",
        "board__name": "ICSE",
        "links": 1,
    },
    {
        "subject__name": "Biolog",
        "klass__name": "12th",
        "medium__name": "Englishmed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 1,
    },
    {
        "subject__name": "Mathematics",
        "klass__name": "8th",
        "medium__name": "Hindimed",
        "category__name": "Solution",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 1,
    },
    {
        "subject__name": "Mathematics",
        "klass__name": "6th",
        "medium__name": "Hindimed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 2,
    },
    {
        "subject__name": "Physics",
        "klass__name": "7th",
        "medium__name": "Hindimed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 1,
    },
    {
        "subject__name": "Physics",
        "klass__name": "7th",
        "medium__name": "Hindimed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "CBSE",
        "links": 1,
    },
    {
        "subject__name": "Chemistr",
        "klass__name": "12th",
        "medium__name": "Hindimed",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 1,
    },
    {
        "subject__name": "Mathematics",
        "klass__name": "12th",
        "medium__name": "ngali",
        "category__name": "Ncert",
        "subject__sub_subject": "null",
        "board__name": "ICSE",
        "links": 1,
    },
]
# print(queryset[2])
q = []


def transform(dd):
    return json.dumps(dd)


l1 = "subject__name"
l2 = "klass__name"
l3 = "medium__name"
l4 = "category__name"
l5 = "subject__sub_subject"
l6 = "board__name"
l7 = "links"
levels = [l1, l2, l3, l4, l5, l6]

a = defaultdict(set)
ap = defaultdict(list)
meta_list = ["subject__sub_subject__meta"]
meta = {i: None for i in meta_list}
# print(meta)


# for i in meta_list:
#     meta[i]
# for data in queryset:
#     for k, v in data.items():
#         if k == 'links':
#             continue
#         a[(k, levels.index(k))].add(v)
#         if k == l1:
#             ap[v].append(data)

# ALL = []


# dic = defaultdict(list)
# cnt = 0
# for data in queryset:
#     for i in range(len(levels)):
#         key = data[levels[i]]
#         if i == len(levels) - 1:
#             dic[key].append(("leaf", i + 1))
#         else:
#             key2 = data[levels[i + 1]]
#             if (key2, i + 1) in dic[key]:
#                 continue
#             dic[key].append((key2, i + 1))
#     cnt += 1


def create_node(name, value=None):  # value = links
    return {"name": name, "value": value, "data": []}


def add_child(node, obj):
    node["data"].append(obj)


node = create_node("root")
count = 0
for data in queryset:
    if count == 3:
        break
    in_order = []
    for level in levels:
        if level == l3:
            in_order.append(data[level] + "med")
        else:
            in_order.append(data[level])
    # f = {: None for i in levels}
    # print(f)

    def func(key, par):
        ok = True
        for k in par["data"]:
            if k["name"] == key:
                ok = False

        if ok:
            add_child(par, create_node(key))

        if not in_order:
            return
        idx = 0
        val = in_order.pop(0)

        for k in par["data"]:
            if k["name"] == key:
                # print(val)
                func(val, par["data"][idx])
            idx += 1

    func(in_order.pop(0), node)
    count += 1
print(transform(node))


# print(transform(node))
# print(transform(dic))
# for subject in a[(l1, 0)]:
#     node = create_node(subject)

#     add_child(node, add_child())

# node = create_node('Math')
# add_child(node, create_node('CBSE',"ok"))
# add_child(node['data'][0])
# add_child(node['data'][1], create_node('pp'))
# print(transform(node))

"""
vis = set()
def func(dic,key, node):
    for j in dic[key]:
        if j in vis:
            continue
        add_child(node, create_node(j))

"""
# print(node)
# print(node1)

# print(transform(node))


# A = []

# for subjects in a[(l1, 0)]:
#     for data in ap[subjects]:
#         alls = [0] * 6

# A.append({})

# res = A[-1]
# tree = res
# for l in levels:
#     tree["key"] = "key"
#     tree["links"] = "link"
#     tree["data"] = [{}]
#     tree = tree["data"][0]

# res = A[-1]
# tree = res

# for k, v in data.items():
#     if k == "links":
#         continue
#     tree["key"] = v
#     tree = tree["data"][0]
# print(A[-1])
# print()

# print(transform(A))


# print(a)
# result = {}
# for i in range(len(queryset)):
#     for k1, k2 in dic:
#         if k2 == i:
#             # result[]
#             pass
# allres = [{}]
# res = allres[0]
# tree = res
# for l in levels:
#     tree["key"] = "key"
#     tree["links"] = "link"
#     tree["data"] = [{}]
#     tree = tree["data"][0]


# print(transform(A))
# print(transform(allres))


# for i in range(5):
#     print()

# exist(dic, '12th')

# pprint(ALL)

# sorted_dic = sorted(dic.items(), key=lambda x: x[1])
# print(sorted_dic[0])
# import json
# r = json.dumps(sorted_dic)
# print(r)
# level , next level

# result = [{}]
# for i in range(1,len(levels)):
#     all_taken = set()
#     tree = result[-1]
#     for key in dic:
#         for val in dic[key]:
#             if val[1] == i :
#                 if key not in all_taken:

#                     # result.append({})
#                     # tree = result[-1]
#                     # tree["key"] = key


# ALL = []


def check(level, tree, cnt=-1):
    while cnt < level:
        cnt += 1
        if "data" in tree:
            for t in tree["data"]:
                check(level, t, cnt)

    if cnt == level:
        ALL.append(tree)

    # if cnt == level:
    #     return (True, tree)
    # return (False, tree)


result = {}
# for data in queryset:
#     for k, v in data.items():


# print(transform(result))
# for subject in a[(l1, 0)]:
#     subject = 'Physics'
#     node = create_node(subject)
#     vis = set()

#     def func(dic, key, par, level):
#         idx = 0
#         vis.add(key)
#         for j in dic[key]:
#             if j[0] in vis:
#                 continue
#             if j[1] != level + 1:
#                 continue
#             add_child(par, create_node(j[0]))
#             idx = 0
#             for kk in par['data']:
#                 if kk['name'] == j[0]:
#                     func(dic, j[0], par['data'][idx], level + 1)
#                 idx += 1

#     func(dic, subject, node, 0)
#     # print(node)
#     print(transform(node))
#     break
