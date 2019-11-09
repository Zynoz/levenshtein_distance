import numpy as np
import pandas as pd


def minimum_edit_distance(s1, s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2+1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             new_distances[-1])))
        distances = new_distances
    return distances[-1]


if __name__ == '__main__':

    data = pd.read_csv('E:\\Downloads\\MOCK_DATA.csv', header=None)  # path to data to cluster remove 'header=None' if data has header
    threshold = 1  # max distance between data
    threshold_amount = 4  # min amount of clustered data per data

    order_numbers = data[0].tolist()

    count = 0
    best_matches = []
    above_threshold = []
    print('----------clustering starting----------')
    for order_number_outside in order_numbers:
        current_matches = []
        count = count + 1
        for order_number_inside in reversed(order_numbers):
            distance = minimum_edit_distance(order_number_outside, order_number_inside)
            if distance <= threshold:
                current_matches.append(order_number_inside)

        best_matches.append(current_matches)
    unique_best_matches = []
    #  make matches unique
    for best in best_matches:
        if best not in unique_best_matches:
            unique_best_matches.append(best)
    #  filter for threshold_amount
    for unique_best in unique_best_matches:
        if len(unique_best) >= threshold_amount:
            above_threshold.append(unique_best)
    #  print list
    for x in above_threshold:
        print(x)
    print('----------clustering done----------')
