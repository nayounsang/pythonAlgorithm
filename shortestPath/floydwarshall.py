def floyd(mat):
    length = len(mat)
    result = [[0] * length for _ in range(length)]  # 결과를 담을 2차원 리스트
    for i in range(length):
        for j in range(length):
            result[i][j] = mat[i][j]
    for through in range(length):  # 경유점
        for start in range(length):  # 시작점
            for end in range(length):  # 종점
                result[start][end] = min(result[start][end], result[start][through] + result[through][end])
    return result
