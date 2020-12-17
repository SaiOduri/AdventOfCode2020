def transformFileIntoArray(f):
    with open(f, "r") as f:
        arr = [x.strip('\n') for x in f]
    return arr

def check_policy(input):
    policies = transformFileIntoArray(input)
    count = 0
    total_count = 0
    for policy in policies:
        options = policy.split(" ")
        for letter in options[2]:
            if letter in options[1]:
                count +=  1
        minmax = options[0].split('-')
        if(count >= int(minmax[0]) and count <= int(minmax[1])):
            total_count += 1
        count = 0
    return total_count

def new_policy(input):
    policies = transformFileIntoArray(input)
    count = 0
    total_count = 0
    for policy in policies:
        options = policy.split(" ")
        minmax = options[0].split('-')
        lower = int(minmax[0])
        upper  = int(minmax[1])
        if(bool(options[2][lower-1] in options[1]) != bool(options[2][upper-1] in options[1])):
            count += 1
    return count
