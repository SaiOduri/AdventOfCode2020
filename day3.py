def transformFileIntoArray(f):
    with open(f, "r") as f:
        arr = [x.strip('\n') for x in f]
    return arr

def day3(input):
    rows = transformFileIntoArray(input)
    count = 0
    tree_count = 0
    for row in rows:
        newrow = row*10000
        if(newrow[count] == "#"):
            tree_count += 1
        count += 7
    return tree_count

def day3_part2(input):
    rows = transformFileIntoArray(input)
    count = 0
    tree_count = 0
    skip = False
    for row in rows:
        if(not skip):
            newrow = row*10000
            if(newrow[count] == "#"):
                tree_count += 1
            count += 
        skip = not skip
    return tree_count

# Proper Solution:

with open("day3_input.txt") as input:
    lines = input.readlines()
    counts = []
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x = y = 0
        count = 0
        while y <= len(lines) - 1:
            loc = lines[y][x]
            if loc == "#":
                count += 1
            x = x + right
            if x >= len(lines[0]) - 1:
                x = x - len(lines[0]) + 1
            y = y + down
        counts.append(count)
    print(counts)
    ans = 1
    for count in counts:
        ans *= count
    print(ans)