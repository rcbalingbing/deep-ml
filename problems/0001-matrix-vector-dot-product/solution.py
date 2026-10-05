def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	
	# Each row must have the same length as the vector
    if any(len(row) != len(b) for row in a):
        return -1

    result = []
    for row in a:
        total = 0
        for x, y in zip(row, b):
            total += x * y
        result.append(total)

    return result
