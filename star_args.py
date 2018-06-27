def print_backwards(*args):
    for word in args[::-1]:
        print(word[::-1], end=' ')

print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader")
