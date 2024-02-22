def bubble_sort(in_t):
    '''
    >>> bubble_sort([])
    []
    >>> bubble_sort([71])
    [71]
    >>> bubble_sort([71, 65, 39, 38, 38, 19, 42, 85, 33])
    [19, 33, 38, 38, 39, 42, 65, 71, 85]
    >>> bubble_sort([8, 5, 3, 5, 5, 4, 10, 7, 2])
    [2, 3, 4, 5, 5, 5, 7, 8, 10]
    >>> bubble_sort([8, 9, 10, 8, 7, 4, 2, 4, 9])
    [2, 4, 4, 7, 8, 8, 9, 9, 10]
    '''
    # print(in_t)
    if len(in_t) <= 1:
        return in_t

    sort = True
    max = len(in_t) - 1
    last_changed_index = None
    while sort:
        last_changed_index = max
        for i in range(max):
            if in_t[i] > in_t[i + 1]:
                in_t[i], in_t[i + 1] = in_t[i + 1], in_t[i]
                last_changed_index = i
        max -= 1
        if last_changed_index < max:
            max = last_changed_index
        if max == 0:
            sort = False
    return in_t


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    # import random
    #
    # print(bubble_sort([random.randint(1, 1000) for i in range(1, 1000)]))
