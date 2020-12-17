with open("day5_input.txt", "r") as fp:
    lines = fp.readlines()

lines = [line[:-1] for line in lines]

seat_ids = []
for line in lines:
    r = line[:7]
    start = 0
    end = 127
    row, col = 0, 0
    for char in r:
        if char == "F":
            end = int((start+end+1)/2) - 1
        elif char == "B":
            start = int((start+end+1)/2)
    row = start
    r = line[7:]
    start = 0
    end = 7
    for char in r:
        if char == "L":
            end = int((start+end+1)/2) - 1
        elif char == "R":
            start = int((start+end+1)/2)
    col = start
    sid = row*8 + col
    seat_ids.append(sid)

print("Part 1:", max(seat_ids))
print("Part 2:", [seat for seat in range(min(seat_ids), max(seat_ids)) if seat not in seat_ids][0])