with open("day9_input.txt", "r") as f:
    data = [int(x.strip('\n')) for x in f]

i = 0
found = False
for j in range(25, len(data)):
    preamble = data[i:i+25]
    current = data[j]
    for val in preamble:
        difference = current - val
        if(difference in preamble):
            found = True
    if(not found):
        print("Part 1:", current)
        c = current
    found = False
    i += 1

sum = 0
vals = []
for i in range(len(data)):
    for j in range(i+1,len(data)):
        sum += data[j]
        vals.append(data[j])
        if(sum > c):
            vals.clear()
            sum = 0
            break
        if(sum == c and (min(vals) != max(vals))):
            print("Part 2:", min(vals) + max(vals))
