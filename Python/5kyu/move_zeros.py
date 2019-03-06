def move_zeros(array):
    result = []
    zeros = 0
    for i in array:
        if (i == 0 and not isinstance(i, bool)):
            zeros += 1
        else:
            result.append(i)
    for i in range(zeros):
        result.append(0)
    return result