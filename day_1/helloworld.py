import math

print(type(10))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(1+3j))


def euclidean_diff(p1, p2, q1, q2):
    diff = math.sqrt((p1-q1)**2 + (p2 - q2)**2)
    return diff

print(euclidean_diff(2, 3, 10, 8))

