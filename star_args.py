def average(*args):
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(average(1, 2, 3, 4))
