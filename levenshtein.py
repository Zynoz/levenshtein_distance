import pandas as pd


# noinspection PyMethodMayBeStatic
class LevenshteinCluster(object):

    def _minimum_edit_distance(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        distances = range(len(s1) + 1)
        for index2, char2 in enumerate(s2):
            new_distances = [index2 + 1]
            for index1, char1 in enumerate(s1):
                if char1 == char2:
                    new_distances.append(distances[index1])
                else:
                    new_distances.append(1 + min((distances[index1],
                                                  distances[index1 + 1],
                                                  new_distances[-1])))
            distances = new_distances
        return distances[-1]

    def cluster_strings(self, path, index_of_data_column, threshold_distance=1, threshold_amount=4):
        if path is None:
            raise FileNotFoundError('Path is empty')
        data = pd.read_csv(path)  # path to data to cluster remove 'header=None' if data has header

        print(index_of_data_column)
        order_numbers = data[index_of_data_column].tolist()

        count = 0
        best_matches = []
        above_threshold = []
        for order_number_outside in order_numbers:
            current_matches = []
            count = count + 1
            for order_number_inside in reversed(order_numbers):
                distance = self._minimum_edit_distance(order_number_outside, order_number_inside)
                if distance <= threshold_distance:
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
        return above_threshold


if __name__ == '__main__':
    levenshtein = LevenshteinCluster()
    cluster = levenshtein.cluster_strings('E:\\Downloads\\MOCK_DATA.csv', index_of_data_column='names')
    for x in cluster:
        print(x)
