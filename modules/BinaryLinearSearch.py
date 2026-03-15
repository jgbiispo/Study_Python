def linear_searh(lst: list, target) -> int:
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1


lst = [5, 3, 8, 1, 9, 2, 7]
print(linear_searh(lst, 9))
print(linear_searh(lst, 99))
