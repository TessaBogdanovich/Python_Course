# x1 = lambda x: x
# x1(5)
# def x1(x):
#     return x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#  print("ok")
# else:
#  print("fail")

49.
def find_farthest_orbit(list1):
    max_elips = max(list1, key = lambda x: (x[0] * x[1]) * (x[0] != x[1]))
    return max_elips
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))