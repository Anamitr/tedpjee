from sklearn.model_selection import train_test_split
import numpy as np


def divide_set(classes, training_part_procentage):
    all_data = trim_and_label_data(classes)
    X_train, X_test, y_train, y_test = train_test_split(all_data[1:].T, all_data[:1].T,
                                                        test_size=training_part_procentage, random_state=42)
    return X_train, X_test, y_train, y_test


def trim_and_label_data(classes):
    classA = np.insert(classes[0], 0, np.array([0 for i in classes[0][0]]), 0)
    classB = np.insert(classes[1], 0, np.array([1 for i in classes[1][0]]), 0)
    all_data = np.append(classA, classB, 1)
    chosen_rows = [x + 1 for x in [0, 1, 2, 3, 4]]
    chosen_rows.insert(0, 0)
    return all_data[chosen_rows]  # all_data[[x+1 for x in GlobalVariables.CHOSEN_FEATURES].append(0)]


def classify_one_with_kNN(x, y, x_test, k):
    results = []
    for j in range(0, len(x)):
        results.append([np.linalg.norm(x_test - x[j]), j, y[j]])
    results = np.array(results)
    results = results[results[:, 0].argsort()]

    return results[0:k]
