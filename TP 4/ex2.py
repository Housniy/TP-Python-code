dict1 = {"a": 10, "b": "test"}
dict2 = {"a": 5, "c": "data"}

def add_dicts(dict1, dict2):
    dict1_keys = dict1.keys()
    dict2_keys = dict2.keys()
    all_keys = list(dict1_keys) + list(dict2_keys)

    dict3 = {}
    for i, key in enumerate(all_keys):
        dict3[key] = dict1.get(key, "") + dict2.get(key, "")

    sorted_dict = {}
    list_keys = []
    for i, key in enumerate(dict3):
        list_keys.append(key)

    list_keys.sort()

    for i, key in enumerate(list_keys):
        sorted_dict[key] = dict3[key]

    print(sorted_dict)


add_dicts(dict1, dict2)