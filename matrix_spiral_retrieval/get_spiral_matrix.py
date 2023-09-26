from matrix_spiral_retrieval.utils import transform_matrix_to_normal


async def get_spiral_list(url: str = None, filepath: str = None):
    matrix = await transform_matrix_to_normal(url, filepath)

    spiral_list = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(top, bottom + 1):
                spiral_list.append(matrix[i][left])
            left += 1

        elif direction == 1:
            for i in range(left, right + 1):
                spiral_list.append(matrix[bottom][i])
            bottom -= 1

        elif direction == 2:
            for i in reversed(range(top, bottom + 1)):
                spiral_list.append(matrix[i][right])
            right -= 1

        elif direction == 3:
            for i in reversed(range(left, right + 1)):
                spiral_list.append(matrix[top][i])
            top += 1

        direction = (direction + 1) % 4

    return spiral_list
