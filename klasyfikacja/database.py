import numpy as np

from feature_maps import feature_map_list


def getClassesWithNamesAndNumOfTraits():
    classes = []
    classes_names = []
    num_of_traits = int

    with open("klasyfikacja.txt", "r") as file:
        data = file.readlines()
        num_of_traits = len(data[0].split(" "))

        for row in data:
            row = row.replace("\n", "")
            row = row.split(" ")
            class_name = row[num_of_traits - 1]
            del row[num_of_traits - 1]
            del row[0:2]

            row_mapped = [feature_map_list[i][row[i]] for i in range(len(row))]

            if class_name not in classes_names:
                classes_names.append(class_name)
                classes.append([])
            classes[classes_names.index(class_name)].append(row_mapped)
    classes[0] = np.transpose(np.array(classes[0]))
    classes[1] = np.transpose(np.array(classes[1]))
    return [classes, classes_names, num_of_traits]


def load_test_examples():
    results = []
    with open("test.txt", "r") as file:
        data = file.readlines()
        for row in data:
            row = row.replace("\n", "")
            row = row.split(" ")
            del row[0:2]
            row_mapped = [feature_map_list[i][row[i]] for i in range(len(row))]
            results.append(row_mapped)
    return results
