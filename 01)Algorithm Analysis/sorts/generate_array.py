import random
def generate_list(n = 20):
    arr = []
    for _ in range(n):
        arr.append((random.randint(0, 5)))
    return arr
