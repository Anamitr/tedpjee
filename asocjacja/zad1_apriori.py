import itertools


def import_data(file_name: str):
    data = []
    file = open(file_name, 'r')
    for line in file:
        # line = line.replace("]", "").replace("[", "")
        line = line.translate({ord(i): None for i in ['[', ']', '\ufeff']})
        transaction = line.strip().split(', ')
        data.append(transaction)
    return data


def get_distinct_items():
    distinct_items = []
    for transaction in data:
        for item in transaction:
            if item not in distinct_items:
                distinct_items.append(item)
    return distinct_items


def get_frequency_dict(collections):
    freq_dict = {}
    for collection in collections:
        collection_counter = 0
        for transaction in data:
            if type(collection) is str:
                if collection in transaction:
                    collection_counter += 1
            elif set(collection).issubset(set(transaction)):  # set(collection).issubset(set(transaction))
                collection_counter += 1

        freq_dict[collection] = collection_counter
    return freq_dict


def delete_not_frequent_collections(frequency_dict):
    frequent_collection_dict = {}
    for collection in frequency_dict.keys():
        if frequency_dict[collection] >= SUPPORT_THRESHOLD * number_of_transactions:
            frequent_collection_dict[collection] = frequency_dict[collection]
    return frequent_collection_dict


def self_joint(old_collections):
    old_collections = [item for item in old_collections]
    number_of_first_objects = len(old_collections[0]) - 1
    firsts = set([item[:number_of_first_objects] for item in old_collections])
    new_collections = []
    for first_objects in firsts:
        following = []
        for collection in old_collections:
            if collection[:number_of_first_objects] == first_objects:
                following.append(collection[number_of_first_objects:][0])

        following_combinations = [combination for combination in itertools.combinations(following, 2)]

        for item in following_combinations:
            new_collections.append(first_objects + item)

    return new_collections


SUPPORT_THRESHOLD = 0.01
GIVEN_K_LENGTH = 4

# data = import_data('asocjacja_demo.txt')
data = import_data('asocjacja.txt')
number_of_transactions = len(data)
print(data)

k = 1
distinct_items = get_distinct_items()
print(distinct_items)
collections = distinct_items

while True:
    print("k =", k)
    frequency_dict = get_frequency_dict(collections)
    print("frequency_dict:", frequency_dict)
    frequent_collection_dict = delete_not_frequent_collections(frequency_dict)
    print("frequent_collection_dict:", frequent_collection_dict)
    if k == GIVEN_K_LENGTH:

        print("The end")
        break
    k += 1
    if k < 3:
        collections = [combination for combination in itertools.combinations(frequent_collection_dict.keys(), k)]
    else:
        collections = self_joint(frequent_collection_dict.keys())
    print("new collections:", collections)

