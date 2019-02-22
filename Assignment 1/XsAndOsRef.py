from typing import List


def checkio(game_result: List[str]) -> str:
    result = "D"
    if game_result[0][0] == game_result[1][1]\
    and game_result[0][0] == game_result[2][2]:
        result = game_result[0][0]
    if game_result[0][2] == game_result[1][1]\
    and game_result[0][2] == game_result[2][0]:
        result = game_result[0][2]
    if result == "D":
        for x in range(3):
            if game_result[0][x] == game_result[1][x] \
            and game_result[0][x] == game_result[2][x]:
                result = game_result[0][x]
    if result == "D":
        for y in range(3):
            if game_result[y][0] == game_result[y][1] \
            and game_result[y][0] == game_result[y][2]:
                result = game_result[y][0]
    if result == ".":
        result = "D"
    return result


ex1 = ["X.O",
       "XX.",
       "XOO"]  # == X
ex2 = ["OO.",
       "XOX",
       "XOX"]  # == O
ex3 = ["OOX",
       "XXO",
       "OXX"]  # == D
ex4 = ["O.X",
       "XX.",
       "XOO"]  # == X

print(checkio(ex1))
print(checkio(ex2))
print(checkio(ex3))
print(checkio(ex4))
