def average(*args):
    print(type(args))
    print("args is {}".format(args))
    print("*args is: ", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    return tuple(args)


print(average(1, 2, 3, 4))


message_tuple = build_tuple("hello", "planet", "earth", "take")
print(type(message_tuple))
print(message_tuple)