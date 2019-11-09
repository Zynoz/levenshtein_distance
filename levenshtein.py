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

    data = pd.read_csv('E:\\Downloads\\MOCK_DATA.csv', header=None)

    order_numbers = data[0].tolist()

    print(order_numbers)
    count = 0
    best_matches = []
    for order_number_outside in order_numbers:
        current_matches = []
        count = count + 1
        for order_number_inside in reversed(order_numbers):
            distance = minimum_edit_distance(order_number_outside, order_number_inside)
            if distance < 3:
                # print(order_number_outside, 'is compatible with', order_number_inside, 'with a distance of ', distance)
                current_matches.append(order_number_inside)
            else:
                print(order_number_outside, 'is not compatible with', order_number_inside, 'with a distance of ', distance)
        best_matches.append(current_matches)
    print(count)
    unique_best_matches = []
    for best in best_matches:
        if best not in unique_best_matches:
            unique_best_matches.append(best)
    for best in unique_best_matches:
        print(best)
    print(len(best_matches))
