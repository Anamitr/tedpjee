import copy
import numpy as np

import classifier
import database

TRAIN_SET_RATIO = 0.2
NUM_OF_FEATURES_TO_CHOOSE = 3
NUM_OF_CROSSVALIDATION_ITERATIONS = 10
NUM_OF_ALL_FEATURES = 5
CHOSEN_FEATURES = [0, 1, 2, 3, 4]

classes, classes_names, num_of_traits = database.getClassesWithNamesAndNumOfTraits()
test_examples = database.load_test_examples()

original_classes = copy.deepcopy(classes)

X_train, X_test, y_train, y_test = classifier.divide_set(classes, TRAIN_SET_RATIO)

x = np.concatenate((X_train, X_test))
y = np.concatenate((y_train, y_test))

results = classifier.classify_one_with_kNN(x, y, test_examples[0], 3)
print(results)
results = classifier.classify_one_with_kNN(x, y, test_examples[1], 3)
print(results)
