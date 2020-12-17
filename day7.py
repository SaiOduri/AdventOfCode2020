data = open('day7_input.txt', 'r').read().splitlines()

rules = {}

def day7():
    for d in data:
        x = d[:-1].split(' contain ')
        c_color = x[0][:-5]
        for b in x[1].split(', '):
            if b != 'no other bags':
                color = ' '.join(b.split(' ')[1:-1])
                if color not in rules:
                    rules[color] = set({})
                rules[color].add(c_color)
    
    colors = {'shiny gold'}
    added = True
    while added:
        added = False
        l = len(colors)
        for color in colors:
            if color in rules:
                colors = colors | rules[color]
        if len(colors) > l:
            added = True

    return (len(colors) - 1)

def day7_part2(): 
    for d in data:
        x = d[:-1].split(' contain ')
        c_color = x[0][:-5]
        for b in x[1].split(', '):
            if b != 'no other bags':
                color = ' '.join(b.split(' ')[1:-1])
                num = int(b.split(' ')[0])
                if c_color not in rules:
                    rules[c_color] = set({})
                rules[c_color].add((color, num))
            else:
                rules[c_color] = set({})
    
    def add_colors(color):
        total = 0
        for o_color, num in rules[color]:
            total += num * (1 + add_colors(o_color))
        return total

    return (add_colors('shiny gold'))

print("Part 1:", day7())
print("Part 2:", day7_part2())
