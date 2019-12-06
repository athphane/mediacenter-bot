def split_list(input_list, n):
    """
    Takes a list and splits it into smaller lists of n elements each.
    :param input_list:
    :param n:
    :return:
    """
    n = max(1, n)
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]
