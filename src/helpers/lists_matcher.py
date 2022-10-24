def return_list_match(list_a, list_b):
    # return [i for i, j in zip(list_a, list_b) if i == j]
    return list(set(list_a).intersection(list_b))


def return_list_no_match(list_a, list_b):
    return list(set(list_a).difference(list_b))
