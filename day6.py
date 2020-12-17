with open('day6_input.txt', 'r') as file:
    data = file.read().split('\n\n')

def part_one(data):
    return sum(len(set.union(*[set(s) for s in group.split()])) for group in data)


def part_two(data):
    return sum(len(set.intersection(*[set(s) for s in group.split()])) for group in data)


print("Part 1:", part_one(data))
print("Part 2:", part_two(data))